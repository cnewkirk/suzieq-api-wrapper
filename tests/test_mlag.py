"""Tests for MlagMixin – /api/v2/mlag."""
import responses

from .conftest import API, qs
from .fixtures import MLAG_SHOW


@responses.activate
def test_show_mlag_no_filters(client):
    responses.add(responses.GET, f"{API}/mlag/show", json=MLAG_SHOW)
    result = client.show_mlag()
    assert result == MLAG_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_mlag_namespace_filter(client):
    responses.add(responses.GET, f"{API}/mlag/show", json=MLAG_SHOW)
    client.show_mlag(namespace=["datacenter1"])
    params = qs(responses.calls[0].request.url)
    assert params["namespace"] == ["datacenter1"]


@responses.activate
def test_show_mlag_hostname_filter(client):
    responses.add(responses.GET, f"{API}/mlag/show", json=MLAG_SHOW)
    client.show_mlag(hostname=["leaf01"])
    params = qs(responses.calls[0].request.url)
    assert params["hostname"] == ["leaf01"]


@responses.activate
def test_show_mlag_query_str(client):
    responses.add(responses.GET, f"{API}/mlag/show", json=MLAG_SHOW)
    client.show_mlag(query_str="state == 'up'")
    params = qs(responses.calls[0].request.url)
    assert params["query_str"] == ["state == 'up'"]


@responses.activate
def test_show_mlag_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/mlag/show", json=MLAG_SHOW)
    client.show_mlag()
    params = qs(responses.calls[0].request.url)
    assert "namespace" not in params
    assert "hostname" not in params
    assert "query_str" not in params


@responses.activate
def test_summarize_mlag(client):
    responses.add(responses.GET, f"{API}/mlag/summarize", json={})
    result = client.summarize_mlag()
    assert result == {}


@responses.activate
def test_unique_mlag(client):
    responses.add(responses.GET, f"{API}/mlag/unique", json=[])
    client.unique_mlag(what="state")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["state"]


@responses.activate
def test_top_mlag(client):
    responses.add(responses.GET, f"{API}/mlag/top", json=MLAG_SHOW)
    client.top_mlag(what="state", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["state"]
    assert params["count"] == ["5"]
