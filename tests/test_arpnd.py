"""Tests for ArpndMixin – /api/v2/arpnd."""
import responses

from .conftest import API, qs
from .fixtures import ARPND_SHOW


@responses.activate
def test_show_arpnd_no_filters(client):
    responses.add(responses.GET, f"{API}/arpnd/show", json=ARPND_SHOW)
    result = client.show_arpnd()
    assert result == ARPND_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_arpnd_ip_filter(client):
    responses.add(responses.GET, f"{API}/arpnd/show", json=ARPND_SHOW)
    client.show_arpnd(ipAddress=["10.0.0.2"])
    params = qs(responses.calls[0].request.url)
    assert params["ipAddress"] == ["10.0.0.2"]


@responses.activate
def test_show_arpnd_macaddr_filter(client):
    responses.add(responses.GET, f"{API}/arpnd/show", json=ARPND_SHOW)
    client.show_arpnd(macaddr=["aa:bb:cc:dd:ee:ff"])
    params = qs(responses.calls[0].request.url)
    assert params["macaddr"] == ["aa:bb:cc:dd:ee:ff"]


@responses.activate
def test_show_arpnd_oif_filter(client):
    responses.add(responses.GET, f"{API}/arpnd/show", json=ARPND_SHOW)
    client.show_arpnd(oif=["swp1"])
    params = qs(responses.calls[0].request.url)
    assert params["oif"] == ["swp1"]


@responses.activate
def test_show_arpnd_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/arpnd/show", json=ARPND_SHOW)
    client.show_arpnd()
    params = qs(responses.calls[0].request.url)
    assert "ipAddress" not in params
    assert "macaddr" not in params
    assert "oif" not in params


@responses.activate
def test_summarize_arpnd(client):
    responses.add(responses.GET, f"{API}/arpnd/summarize", json={})
    result = client.summarize_arpnd()
    assert result == {}


@responses.activate
def test_unique_arpnd(client):
    responses.add(responses.GET, f"{API}/arpnd/unique", json=[])
    client.unique_arpnd(what="oif")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["oif"]


@responses.activate
def test_top_arpnd(client):
    responses.add(responses.GET, f"{API}/arpnd/top", json=ARPND_SHOW)
    client.top_arpnd(what="ipAddress", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["ipAddress"]
    assert params["count"] == ["5"]
