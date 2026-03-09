"""Tests for MacMixin – /api/v2/mac."""
import responses

from .conftest import API, qs
from .fixtures import MAC_SHOW


@responses.activate
def test_show_mac_no_filters(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    result = client.show_mac()
    assert result == MAC_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_mac_macaddr_filter(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    client.show_mac(macaddr=["aa:bb:cc:dd:ee:ff"])
    params = qs(responses.calls[0].request.url)
    assert params["macaddr"] == ["aa:bb:cc:dd:ee:ff"]


@responses.activate
def test_show_mac_vlan_filter(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    client.show_mac(vlan=["100"])
    params = qs(responses.calls[0].request.url)
    assert params["vlan"] == ["100"]


@responses.activate
def test_show_mac_remoteVtepIp_filter(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    client.show_mac(remoteVtepIp=["10.0.1.2"])
    params = qs(responses.calls[0].request.url)
    assert params["remoteVtepIp"] == ["10.0.1.2"]


@responses.activate
def test_show_mac_moveCount_filter(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    client.show_mac(moveCount=">5")
    params = qs(responses.calls[0].request.url)
    assert params["moveCount"] == [">5"]


@responses.activate
def test_show_mac_local_filter(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    client.show_mac(local="True")
    params = qs(responses.calls[0].request.url)
    assert params["local"] == ["True"]


@responses.activate
def test_show_mac_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/mac/show", json=MAC_SHOW)
    client.show_mac()
    params = qs(responses.calls[0].request.url)
    assert "macaddr" not in params
    assert "vlan" not in params
    assert "remoteVtepIp" not in params


@responses.activate
def test_summarize_mac(client):
    responses.add(responses.GET, f"{API}/mac/summarize", json={})
    result = client.summarize_mac()
    assert result == {}


@responses.activate
def test_unique_mac(client):
    responses.add(responses.GET, f"{API}/mac/unique", json=[])
    client.unique_mac(what="vlan")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["vlan"]


@responses.activate
def test_top_mac(client):
    responses.add(responses.GET, f"{API}/mac/top", json=MAC_SHOW)
    client.top_mac(what="vlan", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["vlan"]
    assert params["count"] == ["10"]
