"""Tests for InventoryMixin – /api/v2/inventory."""
import responses

from .conftest import API, qs
from .fixtures import INVENTORY_SHOW


@responses.activate
def test_show_inventory_no_filters(client):
    responses.add(responses.GET, f"{API}/inventory/show", json=INVENTORY_SHOW)
    result = client.show_inventory()
    assert result == INVENTORY_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_inventory_type_filter(client):
    responses.add(responses.GET, f"{API}/inventory/show", json=INVENTORY_SHOW)
    client.show_inventory(type=["supervisor"])
    params = qs(responses.calls[0].request.url)
    assert params["type"] == ["supervisor"]


@responses.activate
def test_show_inventory_vendor_model(client):
    responses.add(responses.GET, f"{API}/inventory/show", json=INVENTORY_SHOW)
    client.show_inventory(vendor=["Cumulus Networks"], model=["VX"])
    params = qs(responses.calls[0].request.url)
    assert params["vendor"] == ["Cumulus Networks"]
    assert params["model"] == ["VX"]


@responses.activate
def test_show_inventory_serial_filter(client):
    responses.add(responses.GET, f"{API}/inventory/show", json=INVENTORY_SHOW)
    client.show_inventory(serial=["SN0001"])
    params = qs(responses.calls[0].request.url)
    assert params["serial"] == ["SN0001"]


@responses.activate
def test_show_inventory_status_filter(client):
    responses.add(responses.GET, f"{API}/inventory/show", json=INVENTORY_SHOW)
    client.show_inventory(status="present")
    params = qs(responses.calls[0].request.url)
    assert params["status"] == ["present"]


@responses.activate
def test_show_inventory_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/inventory/show", json=INVENTORY_SHOW)
    client.show_inventory()
    params = qs(responses.calls[0].request.url)
    assert "type" not in params
    assert "serial" not in params
    assert "status" not in params


@responses.activate
def test_summarize_inventory(client):
    responses.add(responses.GET, f"{API}/inventory/summarize", json={})
    result = client.summarize_inventory()
    assert result == {}


@responses.activate
def test_unique_inventory(client):
    responses.add(responses.GET, f"{API}/inventory/unique", json=[])
    client.unique_inventory(what="vendor")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["vendor"]


@responses.activate
def test_top_inventory(client):
    responses.add(responses.GET, f"{API}/inventory/top", json=INVENTORY_SHOW)
    client.top_inventory(what="type", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["type"]
    assert params["count"] == ["5"]
