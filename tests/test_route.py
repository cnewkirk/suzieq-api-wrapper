"""Tests for RouteMixin – /api/v2/route."""
import responses

from .conftest import API, qs
from .fixtures import ROUTE_SHOW, ROUTE_LPM


@responses.activate
def test_show_route_no_filters(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    result = client.show_route()
    assert result == ROUTE_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_route_prefix_filter(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    client.show_route(prefix=["10.0.0.0/8"])
    params = qs(responses.calls[0].request.url)
    assert params["prefix"] == ["10.0.0.0/8"]


@responses.activate
def test_show_route_protocol_filter(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    client.show_route(protocol=["bgp"])
    params = qs(responses.calls[0].request.url)
    assert params["protocol"] == ["bgp"]


@responses.activate
def test_show_route_multiple_protocols(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    client.show_route(protocol=["bgp", "ospf"])
    params = qs(responses.calls[0].request.url)
    assert set(params["protocol"]) == {"bgp", "ospf"}


@responses.activate
def test_show_route_prefixlen_comparison(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    client.show_route(prefixlen="<24")
    params = qs(responses.calls[0].request.url)
    assert params["prefixlen"] == ["<24"]


@responses.activate
def test_show_route_vrf_ipvers(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    client.show_route(vrf=["default"], ipvers="4")
    params = qs(responses.calls[0].request.url)
    assert params["vrf"] == ["default"]
    assert params["ipvers"] == ["4"]


@responses.activate
def test_show_route_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/route/show", json=ROUTE_SHOW)
    client.show_route()
    params = qs(responses.calls[0].request.url)
    assert "prefix" not in params
    assert "protocol" not in params
    assert "prefixlen" not in params


@responses.activate
def test_summarize_route(client):
    responses.add(responses.GET, f"{API}/route/summarize", json={})
    result = client.summarize_route()
    assert result == {}


@responses.activate
def test_unique_route(client):
    responses.add(responses.GET, f"{API}/route/unique", json=[])
    client.unique_route(what="protocol")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["protocol"]


@responses.activate
def test_top_route(client):
    responses.add(responses.GET, f"{API}/route/top", json=ROUTE_SHOW)
    client.top_route(what="prefixlen", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["prefixlen"]
    assert params["count"] == ["10"]


@responses.activate
def test_lpm_route(client):
    responses.add(responses.GET, f"{API}/route/lpm", json=ROUTE_LPM)
    result = client.lpm_route(address="10.0.0.5")
    assert result == ROUTE_LPM
    params = qs(responses.calls[0].request.url)
    assert params["address"] == ["10.0.0.5"]


@responses.activate
def test_lpm_route_with_vrf(client):
    responses.add(responses.GET, f"{API}/route/lpm", json=ROUTE_LPM)
    client.lpm_route(address="10.0.0.5", vrf="default")
    params = qs(responses.calls[0].request.url)
    assert params["address"] == ["10.0.0.5"]
    assert params["vrf"] == ["default"]


@responses.activate
def test_lpm_route_none_optional_omitted(client):
    responses.add(responses.GET, f"{API}/route/lpm", json=ROUTE_LPM)
    client.lpm_route(address="10.0.0.5")
    params = qs(responses.calls[0].request.url)
    assert "vrf" not in params
    assert "ipvers" not in params
