"""Tests for OspfMixin – /api/v2/ospf."""
import responses

from .conftest import API, qs
from .fixtures import OSPF_SHOW, OSPF_ASSERT


@responses.activate
def test_show_ospf_no_filters(client):
    responses.add(responses.GET, f"{API}/ospf/show", json=OSPF_SHOW)
    result = client.show_ospf()
    assert result == OSPF_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_ospf_state_filter(client):
    responses.add(responses.GET, f"{API}/ospf/show", json=OSPF_SHOW)
    client.show_ospf(state="full")
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["full"]


@responses.activate
def test_show_ospf_negated_state(client):
    responses.add(responses.GET, f"{API}/ospf/show", json=OSPF_SHOW)
    client.show_ospf(state="!passive")
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["!passive"]


@responses.activate
def test_show_ospf_area_vrf(client):
    responses.add(responses.GET, f"{API}/ospf/show", json=OSPF_SHOW)
    client.show_ospf(area=["0.0.0.0"], vrf=["default"])
    params = qs(responses.calls[0].request.url)
    assert params["area"] == ["0.0.0.0"]
    assert params["vrf"] == ["default"]


@responses.activate
def test_show_ospf_ifname_filter(client):
    responses.add(responses.GET, f"{API}/ospf/show", json=OSPF_SHOW)
    client.show_ospf(ifname=["swp1"])
    params = qs(responses.calls[0].request.url)
    assert params["ifname"] == ["swp1"]


@responses.activate
def test_show_ospf_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/ospf/show", json=OSPF_SHOW)
    client.show_ospf()
    params = qs(responses.calls[0].request.url)
    assert "state" not in params
    assert "area" not in params
    assert "ifname" not in params


@responses.activate
def test_summarize_ospf(client):
    responses.add(responses.GET, f"{API}/ospf/summarize", json={})
    result = client.summarize_ospf()
    assert result == {}


@responses.activate
def test_unique_ospf(client):
    responses.add(responses.GET, f"{API}/ospf/unique", json=[])
    client.unique_ospf(what="state")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["state"]


@responses.activate
def test_top_ospf(client):
    responses.add(responses.GET, f"{API}/ospf/top", json=OSPF_SHOW)
    client.top_ospf(what="area", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["area"]
    assert params["count"] == ["5"]


@responses.activate
def test_assert_ospf_all(client):
    responses.add(responses.GET, f"{API}/ospf/assert", json=OSPF_ASSERT)
    result = client.assert_ospf()
    assert result == OSPF_ASSERT


@responses.activate
def test_assert_ospf_fail_only(client):
    responses.add(responses.GET, f"{API}/ospf/assert", json=[])
    client.assert_ospf(result="fail")
    params = qs(responses.calls[0].request.url)
    assert params["result"] == ["fail"]


@responses.activate
def test_assert_ospf_area_filter(client):
    responses.add(responses.GET, f"{API}/ospf/assert", json=OSPF_ASSERT)
    client.assert_ospf(area=["0.0.0.0"])
    params = qs(responses.calls[0].request.url)
    assert params["area"] == ["0.0.0.0"]
