"""Tests for NetworkMixin – /api/v2/network."""
import responses

from .conftest import API, qs
from .fixtures import NETWORK_FIND


@responses.activate
def test_find_network_address(client):
    responses.add(responses.GET, f"{API}/network/find", json=NETWORK_FIND)
    result = client.find_network(address=["10.0.0.5"])
    assert result == NETWORK_FIND
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"
    params = qs(responses.calls[0].request.url)
    assert params["address"] == ["10.0.0.5"]


@responses.activate
def test_find_network_mac(client):
    responses.add(responses.GET, f"{API}/network/find", json=NETWORK_FIND)
    client.find_network(address=["aa:bb:cc:dd:ee:ff"])
    params = qs(responses.calls[0].request.url)
    assert params["address"] == ["aa:bb:cc:dd:ee:ff"]


@responses.activate
def test_find_network_with_vlan_vrf(client):
    responses.add(responses.GET, f"{API}/network/find", json=NETWORK_FIND)
    client.find_network(address=["10.0.0.5"], vlan="100", vrf="default")
    params = qs(responses.calls[0].request.url)
    assert params["vlan"] == ["100"]
    assert params["vrf"] == ["default"]


@responses.activate
def test_find_network_namespace_filter(client):
    responses.add(responses.GET, f"{API}/network/find", json=NETWORK_FIND)
    client.find_network(address=["10.0.0.5"], namespace=["datacenter1"])
    params = qs(responses.calls[0].request.url)
    assert params["namespace"] == ["datacenter1"]


@responses.activate
def test_find_network_none_optional_omitted(client):
    responses.add(responses.GET, f"{API}/network/find", json=NETWORK_FIND)
    client.find_network(address=["10.0.0.5"])
    params = qs(responses.calls[0].request.url)
    assert "vlan" not in params
    assert "vrf" not in params


@responses.activate
def test_show_network_deprecated(client):
    """Deprecated show verb is still callable."""
    responses.add(responses.GET, f"{API}/network/show", json=[])
    result = client.show_network()
    assert result == []


@responses.activate
def test_summarize_network_deprecated(client):
    responses.add(responses.GET, f"{API}/network/summarize", json={})
    result = client.summarize_network()
    assert result == {}


@responses.activate
def test_unique_network_deprecated(client):
    responses.add(responses.GET, f"{API}/network/unique", json=[])
    client.unique_network(what="namespace")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["namespace"]


@responses.activate
def test_top_network_deprecated(client):
    responses.add(responses.GET, f"{API}/network/top", json=[])
    client.top_network(what="namespace", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["namespace"]
