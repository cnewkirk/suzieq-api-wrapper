"""Tests for BgpMixin – /api/v2/bgp."""
import responses

from .conftest import API, qs
from .fixtures import BGP_SHOW, BGP_SUMMARIZE, BGP_ASSERT, BGP_UNIQUE


@responses.activate
def test_show_bgp_no_filters(client):
    responses.add(responses.GET, f"{API}/bgp/show", json=BGP_SHOW)
    result = client.show_bgp()
    assert result == BGP_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_bgp_state_filter(client):
    responses.add(responses.GET, f"{API}/bgp/show", json=BGP_SHOW)
    result = client.show_bgp(state="Established")
    assert result == BGP_SHOW
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["Established"]


@responses.activate
def test_show_bgp_multiple_namespaces(client):
    responses.add(responses.GET, f"{API}/bgp/show", json=BGP_SHOW)
    client.show_bgp(namespace=["dc1", "dc2"])
    params = qs(responses.calls[0].request.url)
    assert set(params["namespace"]) == {"dc1", "dc2"}


@responses.activate
def test_show_bgp_all_table_params(client):
    responses.add(responses.GET, f"{API}/bgp/show", json=BGP_SHOW)
    client.show_bgp(
        namespace=["datacenter1"],
        hostname=["leaf01"],
        peer=["10.1.0.1"],
        state="Established",
        vrf=["default"],
        asn=["65001"],
        afiSafi="ipv4Unicast",
        view="all",
        columns=["hostname", "peer", "state"],
    )
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["Established"]
    assert params["afiSafi"] == ["ipv4Unicast"]
    assert params["view"] == ["all"]


@responses.activate
def test_show_bgp_none_params_omitted(client):
    """None-valued parameters must not appear in the query string."""
    responses.add(responses.GET, f"{API}/bgp/show", json=BGP_SHOW)
    client.show_bgp()
    params = qs(responses.calls[0].request.url)
    assert "state" not in params
    assert "namespace" not in params
    assert "peer" not in params


@responses.activate
def test_summarize_bgp(client):
    responses.add(responses.GET, f"{API}/bgp/summarize", json=BGP_SUMMARIZE)
    result = client.summarize_bgp()
    assert result == BGP_SUMMARIZE


@responses.activate
def test_unique_bgp(client):
    responses.add(responses.GET, f"{API}/bgp/unique", json=BGP_UNIQUE)
    result = client.unique_bgp(what="state")
    assert result == BGP_UNIQUE
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["state"]


@responses.activate
def test_top_bgp(client):
    responses.add(responses.GET, f"{API}/bgp/top", json=BGP_SHOW)
    result = client.top_bgp(what="numChanges", count="5")
    assert result == BGP_SHOW
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["numChanges"]
    assert params["count"] == ["5"]


@responses.activate
def test_top_bgp_reverse(client):
    responses.add(responses.GET, f"{API}/bgp/top", json=BGP_SHOW)
    client.top_bgp(what="numChanges", count="5", reverse="True")
    params = qs(responses.calls[0].request.url)
    assert params["reverse"] == ["True"]


@responses.activate
def test_assert_bgp_all(client):
    responses.add(responses.GET, f"{API}/bgp/assert", json=BGP_ASSERT)
    result = client.assert_bgp()
    assert result == BGP_ASSERT


@responses.activate
def test_assert_bgp_fail_only(client):
    responses.add(responses.GET, f"{API}/bgp/assert", json=[])
    result = client.assert_bgp(result="fail")
    assert result == []
    params = qs(responses.calls[0].request.url)
    assert params["result"] == ["fail"]


@responses.activate
def test_assert_bgp_negated_state(client):
    responses.add(responses.GET, f"{API}/bgp/assert", json=BGP_ASSERT)
    client.assert_bgp(state="!Established")
    params = qs(responses.calls[0].request.url)
    assert params["state"] == ["!Established"]
