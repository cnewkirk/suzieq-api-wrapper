"""Tests for FsMixin – /api/v2/fs."""
import responses

from .conftest import API, qs
from .fixtures import FS_SHOW


@responses.activate
def test_show_fs_no_filters(client):
    responses.add(responses.GET, f"{API}/fs/show", json=FS_SHOW)
    result = client.show_fs()
    assert result == FS_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_fs_mountPoint_filter(client):
    responses.add(responses.GET, f"{API}/fs/show", json=FS_SHOW)
    client.show_fs(mountPoint=["/"])
    params = qs(responses.calls[0].request.url)
    assert params["mountPoint"] == ["/"]


@responses.activate
def test_show_fs_usedPercent_filter(client):
    responses.add(responses.GET, f"{API}/fs/show", json=FS_SHOW)
    client.show_fs(usedPercent=">80")
    params = qs(responses.calls[0].request.url)
    assert params["usedPercent"] == [">80"]


@responses.activate
def test_show_fs_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/fs/show", json=FS_SHOW)
    client.show_fs()
    params = qs(responses.calls[0].request.url)
    assert "mountPoint" not in params
    assert "usedPercent" not in params


@responses.activate
def test_summarize_fs(client):
    responses.add(responses.GET, f"{API}/fs/summarize", json={})
    result = client.summarize_fs()
    assert result == {}


@responses.activate
def test_unique_fs(client):
    responses.add(responses.GET, f"{API}/fs/unique", json=[])
    client.unique_fs(what="mountPoint")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["mountPoint"]


@responses.activate
def test_top_fs(client):
    responses.add(responses.GET, f"{API}/fs/top", json=FS_SHOW)
    client.top_fs(what="usedPercent", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["usedPercent"]
    assert params["count"] == ["5"]
