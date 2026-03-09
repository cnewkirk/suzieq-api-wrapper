"""Tests for SqPollerMixin – /api/v2/sqPoller."""
import responses

from .conftest import API, qs
from .fixtures import SQPOLLER_SHOW


@responses.activate
def test_show_sqpoller_no_filters(client):
    responses.add(responses.GET, f"{API}/sqPoller/show", json=SQPOLLER_SHOW)
    result = client.show_sqpoller()
    assert result == SQPOLLER_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_sqpoller_service_filter(client):
    responses.add(responses.GET, f"{API}/sqPoller/show", json=SQPOLLER_SHOW)
    client.show_sqpoller(service="bgp")
    params = qs(responses.calls[0].request.url)
    assert params["service"] == ["bgp"]


@responses.activate
def test_show_sqpoller_status_filter(client):
    responses.add(responses.GET, f"{API}/sqPoller/show", json=SQPOLLER_SHOW)
    client.show_sqpoller(status="fail")
    params = qs(responses.calls[0].request.url)
    assert params["status"] == ["fail"]


@responses.activate
def test_show_sqpoller_pollExcdPeriodCount(client):
    responses.add(responses.GET, f"{API}/sqPoller/show", json=SQPOLLER_SHOW)
    client.show_sqpoller(pollExcdPeriodCount=">0")
    params = qs(responses.calls[0].request.url)
    assert params["pollExcdPeriodCount"] == [">0"]


@responses.activate
def test_show_sqpoller_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/sqPoller/show", json=SQPOLLER_SHOW)
    client.show_sqpoller()
    params = qs(responses.calls[0].request.url)
    assert "service" not in params
    assert "status" not in params
    assert "pollExcdPeriodCount" not in params


@responses.activate
def test_summarize_sqpoller(client):
    responses.add(responses.GET, f"{API}/sqPoller/summarize", json={})
    result = client.summarize_sqpoller()
    assert result == {}


@responses.activate
def test_unique_sqpoller(client):
    responses.add(responses.GET, f"{API}/sqPoller/unique", json=[])
    client.unique_sqpoller(what="service")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["service"]


@responses.activate
def test_top_sqpoller(client):
    responses.add(responses.GET, f"{API}/sqPoller/top", json=SQPOLLER_SHOW)
    client.top_sqpoller(what="gatherTime", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["gatherTime"]
    assert params["count"] == ["10"]
