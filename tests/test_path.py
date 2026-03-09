"""Tests for PathMixin – /api/v2/path."""
import responses

from .conftest import API, qs
from .fixtures import PATH_SHOW


@responses.activate
def test_show_path_src_dest(client):
    responses.add(responses.GET, f"{API}/path/show", json=PATH_SHOW)
    result = client.show_path(src="10.0.0.1", dest="10.0.0.5")
    assert result == PATH_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"
    params = qs(responses.calls[0].request.url)
    assert params["src"] == ["10.0.0.1"]
    assert params["dest"] == ["10.0.0.5"]


@responses.activate
def test_show_path_with_vrf(client):
    responses.add(responses.GET, f"{API}/path/show", json=PATH_SHOW)
    client.show_path(src="10.0.0.1", dest="10.0.0.5", vrf="default")
    params = qs(responses.calls[0].request.url)
    assert params["vrf"] == ["default"]


@responses.activate
def test_show_path_with_namespace(client):
    responses.add(responses.GET, f"{API}/path/show", json=PATH_SHOW)
    client.show_path(src="10.0.0.1", dest="10.0.0.5", namespace=["datacenter1"])
    params = qs(responses.calls[0].request.url)
    assert params["namespace"] == ["datacenter1"]


@responses.activate
def test_show_path_none_optional_omitted(client):
    responses.add(responses.GET, f"{API}/path/show", json=PATH_SHOW)
    client.show_path(src="10.0.0.1", dest="10.0.0.5")
    params = qs(responses.calls[0].request.url)
    assert "vrf" not in params
    assert "namespace" not in params


@responses.activate
def test_summarize_path(client):
    responses.add(responses.GET, f"{API}/path/summarize", json={})
    result = client.summarize_path()
    assert result == {}


@responses.activate
def test_unique_path(client):
    responses.add(responses.GET, f"{API}/path/unique", json=[])
    client.unique_path(what="hostname")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["hostname"]


@responses.activate
def test_top_path(client):
    responses.add(responses.GET, f"{API}/path/top", json=PATH_SHOW)
    client.top_path(what="hostname", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["hostname"]
    assert params["count"] == ["5"]
