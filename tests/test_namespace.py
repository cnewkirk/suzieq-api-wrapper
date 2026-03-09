"""Tests for NamespaceMixin – /api/v2/namespace."""
import responses

from .conftest import API, qs
from .fixtures import NAMESPACE_SHOW


@responses.activate
def test_show_namespace_no_filters(client):
    responses.add(responses.GET, f"{API}/namespace/show", json=NAMESPACE_SHOW)
    result = client.show_namespace()
    assert result == NAMESPACE_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_namespace_os_filter(client):
    responses.add(responses.GET, f"{API}/namespace/show", json=NAMESPACE_SHOW)
    client.show_namespace(os=["cumulus"])
    params = qs(responses.calls[0].request.url)
    assert params["os"] == ["cumulus"]


@responses.activate
def test_show_namespace_vendor_model(client):
    responses.add(responses.GET, f"{API}/namespace/show", json=NAMESPACE_SHOW)
    client.show_namespace(vendor=["Cumulus Networks"], model=["VX"])
    params = qs(responses.calls[0].request.url)
    assert params["vendor"] == ["Cumulus Networks"]
    assert params["model"] == ["VX"]


@responses.activate
def test_show_namespace_version_filter(client):
    responses.add(responses.GET, f"{API}/namespace/show", json=NAMESPACE_SHOW)
    client.show_namespace(version="4.4.0")
    params = qs(responses.calls[0].request.url)
    assert params["version"] == ["4.4.0"]


@responses.activate
def test_show_namespace_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/namespace/show", json=NAMESPACE_SHOW)
    client.show_namespace()
    params = qs(responses.calls[0].request.url)
    assert "os" not in params
    assert "vendor" not in params
    assert "version" not in params


@responses.activate
def test_summarize_namespace(client):
    responses.add(responses.GET, f"{API}/namespace/summarize", json={})
    result = client.summarize_namespace()
    assert result == {}


@responses.activate
def test_unique_namespace(client):
    responses.add(responses.GET, f"{API}/namespace/unique", json=[])
    client.unique_namespace(what="os")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["os"]


@responses.activate
def test_top_namespace(client):
    responses.add(responses.GET, f"{API}/namespace/top", json=NAMESPACE_SHOW)
    client.top_namespace(what="version", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["version"]
    assert params["count"] == ["5"]
