"""Tests for TablesMixin – /api/v2/table."""
import responses

from .conftest import API, qs


TABLE_SHOW = [
    {"table": "bgp", "numRecords": 8, "timestamp": 1700000000000},
    {"table": "interface", "numRecords": 64, "timestamp": 1700000000000},
]


@responses.activate
def test_show_tables_no_filters(client):
    responses.add(responses.GET, f"{API}/table/show", json=TABLE_SHOW)
    result = client.show_tables()
    assert result == TABLE_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_tables_table_filter(client):
    responses.add(responses.GET, f"{API}/table/show", json=TABLE_SHOW[:1])
    client.show_tables(table="bgp")
    params = qs(responses.calls[0].request.url)
    assert params["table"] == ["bgp"]


@responses.activate
def test_show_tables_namespace_filter(client):
    responses.add(responses.GET, f"{API}/table/show", json=TABLE_SHOW)
    client.show_tables(namespace=["datacenter1"])
    params = qs(responses.calls[0].request.url)
    assert params["namespace"] == ["datacenter1"]


@responses.activate
def test_show_tables_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/table/show", json=TABLE_SHOW)
    client.show_tables()
    params = qs(responses.calls[0].request.url)
    assert "table" not in params
    assert "namespace" not in params


@responses.activate
def test_summarize_tables(client):
    responses.add(responses.GET, f"{API}/table/summarize", json={})
    result = client.summarize_tables()
    assert result == {}


@responses.activate
def test_unique_tables(client):
    responses.add(responses.GET, f"{API}/table/unique", json=[])
    client.unique_tables(what="table")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["table"]


@responses.activate
def test_top_tables(client):
    responses.add(responses.GET, f"{API}/table/top", json=TABLE_SHOW)
    client.top_tables(what="numRecords", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["numRecords"]
    assert params["count"] == ["5"]
