"""Tests for TopologyMixin – /api/v2/topology."""
import responses

from .conftest import API, qs
from .fixtures import TOPOLOGY_SHOW


@responses.activate
def test_show_topology_no_filters(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    result = client.show_topology()
    assert result == TOPOLOGY_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_topology_via_filter(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    client.show_topology(via=["lldp"])
    params = qs(responses.calls[0].request.url)
    assert params["via"] == ["lldp"]


@responses.activate
def test_show_topology_multiple_via(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    client.show_topology(via=["lldp", "bgp"])
    params = qs(responses.calls[0].request.url)
    assert set(params["via"]) == {"lldp", "bgp"}


@responses.activate
def test_show_topology_peerHostname_filter(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    client.show_topology(peerHostname=["spine01"])
    params = qs(responses.calls[0].request.url)
    assert params["peerHostname"] == ["spine01"]


@responses.activate
def test_show_topology_afiSafi_filter(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    client.show_topology(afiSafi="ipv4Unicast")
    params = qs(responses.calls[0].request.url)
    assert params["afiSafi"] == ["ipv4Unicast"]


@responses.activate
def test_show_topology_area_vrf_asn(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    client.show_topology(area=["0.0.0.0"], vrf=["default"], asn=["65000"])
    params = qs(responses.calls[0].request.url)
    assert params["area"] == ["0.0.0.0"]
    assert params["vrf"] == ["default"]
    assert params["asn"] == ["65000"]


@responses.activate
def test_show_topology_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/topology/show", json=TOPOLOGY_SHOW)
    client.show_topology()
    params = qs(responses.calls[0].request.url)
    assert "via" not in params
    assert "peerHostname" not in params
    assert "afiSafi" not in params


@responses.activate
def test_summarize_topology(client):
    responses.add(responses.GET, f"{API}/topology/summarize", json={})
    result = client.summarize_topology()
    assert result == {}


@responses.activate
def test_unique_topology(client):
    responses.add(responses.GET, f"{API}/topology/unique", json=[])
    client.unique_topology(what="via")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["via"]


@responses.activate
def test_top_topology(client):
    responses.add(responses.GET, f"{API}/topology/top", json=TOPOLOGY_SHOW)
    client.top_topology(what="hostname", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["hostname"]
    assert params["count"] == ["10"]
