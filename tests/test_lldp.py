"""Tests for LldpMixin – /api/v2/lldp."""
import responses

from .conftest import API, qs
from .fixtures import LLDP_SHOW


@responses.activate
def test_show_lldp_no_filters(client):
    responses.add(responses.GET, f"{API}/lldp/show", json=LLDP_SHOW)
    result = client.show_lldp()
    assert result == LLDP_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_lldp_ifname_filter(client):
    responses.add(responses.GET, f"{API}/lldp/show", json=LLDP_SHOW)
    client.show_lldp(ifname=["swp1"])
    params = qs(responses.calls[0].request.url)
    assert params["ifname"] == ["swp1"]


@responses.activate
def test_show_lldp_peerHostname_filter(client):
    responses.add(responses.GET, f"{API}/lldp/show", json=LLDP_SHOW)
    client.show_lldp(peerHostname=["spine01"])
    params = qs(responses.calls[0].request.url)
    assert params["peerHostname"] == ["spine01"]


@responses.activate
def test_show_lldp_peerMacaddr_filter(client):
    responses.add(responses.GET, f"{API}/lldp/show", json=LLDP_SHOW)
    client.show_lldp(peerMacaddr=["bb:cc:dd:ee:ff:01"])
    params = qs(responses.calls[0].request.url)
    assert params["peerMacaddr"] == ["bb:cc:dd:ee:ff:01"]


@responses.activate
def test_show_lldp_use_bond_filter(client):
    responses.add(responses.GET, f"{API}/lldp/show", json=LLDP_SHOW)
    client.show_lldp(use_bond="True")
    params = qs(responses.calls[0].request.url)
    assert params["use_bond"] == ["True"]


@responses.activate
def test_show_lldp_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/lldp/show", json=LLDP_SHOW)
    client.show_lldp()
    params = qs(responses.calls[0].request.url)
    assert "ifname" not in params
    assert "peerHostname" not in params
    assert "peerMacaddr" not in params


@responses.activate
def test_summarize_lldp(client):
    responses.add(responses.GET, f"{API}/lldp/summarize", json={})
    result = client.summarize_lldp()
    assert result == {}


@responses.activate
def test_unique_lldp(client):
    responses.add(responses.GET, f"{API}/lldp/unique", json=[])
    client.unique_lldp(what="peerHostname")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["peerHostname"]


@responses.activate
def test_top_lldp(client):
    responses.add(responses.GET, f"{API}/lldp/top", json=LLDP_SHOW)
    client.top_lldp(what="ifname", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["ifname"]
    assert params["count"] == ["5"]
