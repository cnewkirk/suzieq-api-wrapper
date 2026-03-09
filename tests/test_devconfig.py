"""Tests for DevconfigMixin – /api/v2/devconfig."""
import responses

from .conftest import API, qs
from .fixtures import DEVCONFIG_SHOW


@responses.activate
def test_show_devconfig_no_filters(client):
    responses.add(responses.GET, f"{API}/devconfig/show", json=DEVCONFIG_SHOW)
    result = client.show_devconfig()
    assert result == DEVCONFIG_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_devconfig_section_filter(client):
    responses.add(responses.GET, f"{API}/devconfig/show", json=DEVCONFIG_SHOW)
    client.show_devconfig(section="interfaces")
    params = qs(responses.calls[0].request.url)
    assert params["section"] == ["interfaces"]


@responses.activate
def test_show_devconfig_hostname_filter(client):
    responses.add(responses.GET, f"{API}/devconfig/show", json=DEVCONFIG_SHOW)
    client.show_devconfig(hostname=["leaf01"])
    params = qs(responses.calls[0].request.url)
    assert params["hostname"] == ["leaf01"]


@responses.activate
def test_show_devconfig_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/devconfig/show", json=DEVCONFIG_SHOW)
    client.show_devconfig()
    params = qs(responses.calls[0].request.url)
    assert "section" not in params
    assert "namespace" not in params


@responses.activate
def test_summarize_devconfig(client):
    responses.add(responses.GET, f"{API}/devconfig/summarize", json={})
    result = client.summarize_devconfig()
    assert result == {}


@responses.activate
def test_top_devconfig(client):
    responses.add(responses.GET, f"{API}/devconfig/top", json=DEVCONFIG_SHOW)
    client.top_devconfig(what="hostname", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["hostname"]
    assert params["count"] == ["5"]
