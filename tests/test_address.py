"""Tests for AddressMixin – /api/v2/address."""
import responses

from .conftest import API, qs
from .fixtures import ADDRESS_SHOW, ADDRESS_SUMMARIZE


@responses.activate
def test_show_address_no_filters(client):
    responses.add(responses.GET, f"{API}/address/show", json=ADDRESS_SHOW)
    result = client.show_address()
    assert result == ADDRESS_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_address_ip_filter(client):
    responses.add(responses.GET, f"{API}/address/show", json=ADDRESS_SHOW)
    client.show_address(address=["10.0.0.1"])
    params = qs(responses.calls[0].request.url)
    assert params["address"] == ["10.0.0.1"]


@responses.activate
def test_show_address_ipvers_filter(client):
    responses.add(responses.GET, f"{API}/address/show", json=ADDRESS_SHOW)
    client.show_address(ipvers="4")
    params = qs(responses.calls[0].request.url)
    assert params["ipvers"] == ["4"]


@responses.activate
def test_show_address_vrf_and_ifname(client):
    responses.add(responses.GET, f"{API}/address/show", json=ADDRESS_SHOW)
    client.show_address(vrf=["default"], ifname=["swp1"])
    params = qs(responses.calls[0].request.url)
    assert params["vrf"] == ["default"]
    assert params["ifname"] == ["swp1"]


@responses.activate
def test_show_address_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/address/show", json=ADDRESS_SHOW)
    client.show_address()
    params = qs(responses.calls[0].request.url)
    assert "address" not in params
    assert "ipvers" not in params
    assert "vrf" not in params


@responses.activate
def test_show_address_view_all(client):
    responses.add(responses.GET, f"{API}/address/show", json=ADDRESS_SHOW)
    client.show_address(view="all")
    params = qs(responses.calls[0].request.url)
    assert params["view"] == ["all"]


@responses.activate
def test_summarize_address(client):
    responses.add(responses.GET, f"{API}/address/summarize", json=ADDRESS_SUMMARIZE)
    result = client.summarize_address()
    assert result == ADDRESS_SUMMARIZE


@responses.activate
def test_unique_address(client):
    responses.add(responses.GET, f"{API}/address/unique", json=[])
    client.unique_address(what="ipAddressType")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["ipAddressType"]


@responses.activate
def test_top_address(client):
    responses.add(responses.GET, f"{API}/address/top", json=ADDRESS_SHOW)
    client.top_address(what="ipAddress", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["ipAddress"]
    assert params["count"] == ["10"]


@responses.activate
def test_top_address_reverse(client):
    responses.add(responses.GET, f"{API}/address/top", json=ADDRESS_SHOW)
    client.top_address(what="ipAddress", reverse="True")
    params = qs(responses.calls[0].request.url)
    assert params["reverse"] == ["True"]
