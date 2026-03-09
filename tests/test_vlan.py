"""Tests for VlanMixin – /api/v2/vlan."""
import responses

from .conftest import API, qs
from .fixtures import VLAN_SHOW


@responses.activate
def test_show_vlan_no_filters(client):
    responses.add(responses.GET, f"{API}/vlan/show", json=VLAN_SHOW)
    result = client.show_vlan()
    assert result == VLAN_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_vlan_vlan_filter(client):
    responses.add(responses.GET, f"{API}/vlan/show", json=VLAN_SHOW)
    client.show_vlan(vlan=["100"])
    params = qs(responses.calls[0].request.url)
    assert params["vlan"] == ["100"]


@responses.activate
def test_show_vlan_multiple_vlans(client):
    responses.add(responses.GET, f"{API}/vlan/show", json=VLAN_SHOW)
    client.show_vlan(vlan=["100", "200"])
    params = qs(responses.calls[0].request.url)
    assert set(params["vlan"]) == {"100", "200"}


@responses.activate
def test_show_vlan_state_filter(client):
    responses.add(responses.GET, f"{API}/vlan/show", json=VLAN_SHOW)
    client.show_vlan(state="active")
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["active"]


@responses.activate
def test_show_vlan_vlanName_filter(client):
    responses.add(responses.GET, f"{API}/vlan/show", json=VLAN_SHOW)
    client.show_vlan(vlanName=["prod-vlan"])
    params = qs(responses.calls[0].request.url)
    assert params["vlanName"] == ["prod-vlan"]


@responses.activate
def test_show_vlan_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/vlan/show", json=VLAN_SHOW)
    client.show_vlan()
    params = qs(responses.calls[0].request.url)
    assert "vlan" not in params
    assert "state" not in params
    assert "vlanName" not in params


@responses.activate
def test_summarize_vlan(client):
    responses.add(responses.GET, f"{API}/vlan/summarize", json={})
    result = client.summarize_vlan()
    assert result == {}


@responses.activate
def test_unique_vlan(client):
    responses.add(responses.GET, f"{API}/vlan/unique", json=[])
    client.unique_vlan(what="state")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["state"]


@responses.activate
def test_top_vlan(client):
    responses.add(responses.GET, f"{API}/vlan/top", json=VLAN_SHOW)
    client.top_vlan(what="vlan", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["vlan"]
    assert params["count"] == ["5"]
