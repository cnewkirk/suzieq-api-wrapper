"""Tests for InterfaceMixin – /api/v2/interface."""
import responses

from .conftest import API, qs
from .fixtures import INTERFACE_SHOW, INTERFACE_ASSERT


@responses.activate
def test_show_interface_no_filters(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    result = client.show_interface()
    assert result == INTERFACE_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_interface_state_filter(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    client.show_interface(state="up")
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["up"]


@responses.activate
def test_show_interface_negated_state(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    client.show_interface(state="!down")
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["!down"]


@responses.activate
def test_show_interface_ifname_filter(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    client.show_interface(ifname=["swp1", "swp2"])
    params = qs(responses.calls[0].request.url)
    assert set(params["ifname"]) == {"swp1", "swp2"}


@responses.activate
def test_show_interface_mtu_comparison(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    client.show_interface(mtu=[">1500"])
    params = qs(responses.calls[0].request.url)
    assert params["mtu"] == [">1500"]


@responses.activate
def test_show_interface_vrf_type(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    client.show_interface(vrf=["default"], type=["ethernet"])
    params = qs(responses.calls[0].request.url)
    assert params["vrf"] == ["default"]
    assert params["type"] == ["ethernet"]


@responses.activate
def test_show_interface_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/interface/show", json=INTERFACE_SHOW)
    client.show_interface()
    params = qs(responses.calls[0].request.url)
    assert "state" not in params
    assert "ifname" not in params
    assert "mtu" not in params


@responses.activate
def test_summarize_interface(client):
    responses.add(responses.GET, f"{API}/interface/summarize", json={})
    result = client.summarize_interface()
    assert result == {}


@responses.activate
def test_unique_interface(client):
    responses.add(responses.GET, f"{API}/interface/unique", json=[])
    client.unique_interface(what="state")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["state"]


@responses.activate
def test_top_interface(client):
    responses.add(responses.GET, f"{API}/interface/top", json=INTERFACE_SHOW)
    client.top_interface(what="mtu", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["mtu"]
    assert params["count"] == ["10"]


@responses.activate
def test_assert_interface_all(client):
    responses.add(responses.GET, f"{API}/interface/assert", json=INTERFACE_ASSERT)
    result = client.assert_interface()
    assert result == INTERFACE_ASSERT


@responses.activate
def test_assert_interface_fail_only(client):
    responses.add(responses.GET, f"{API}/interface/assert", json=[])
    client.assert_interface(result="fail")
    params = qs(responses.calls[0].request.url)
    assert params["result"] == ["fail"]


@responses.activate
def test_assert_interface_mtu_check(client):
    responses.add(responses.GET, f"{API}/interface/assert", json=INTERFACE_ASSERT)
    client.assert_interface(what="mtu", value=[9216])
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["mtu"]
    assert params["value"] == ["9216"]


@responses.activate
def test_assert_interface_ignore_missing_peer(client):
    responses.add(responses.GET, f"{API}/interface/assert", json=INTERFACE_ASSERT)
    client.assert_interface(ignore_missing_peer=True)
    params = qs(responses.calls[0].request.url)
    assert params["ignore_missing_peer"] == ["True"]
