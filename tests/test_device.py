"""Tests for DeviceMixin – /api/v2/device."""
import responses

from .conftest import API, qs
from .fixtures import DEVICE_SHOW


@responses.activate
def test_show_device_no_filters(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    result = client.show_device()
    assert result == DEVICE_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_device_os_filter(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    client.show_device(os=["cumulus"])
    params = qs(responses.calls[0].request.url)
    assert params["os"] == ["cumulus"]


@responses.activate
def test_show_device_status_filter(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    client.show_device(status=["alive"])
    params = qs(responses.calls[0].request.url)
    assert params["status"] == ["alive"]


@responses.activate
def test_show_device_vendor_model(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    client.show_device(vendor=["Cumulus Networks"], model=["VX"])
    params = qs(responses.calls[0].request.url)
    assert params["vendor"] == ["Cumulus Networks"]
    assert params["model"] == ["VX"]


@responses.activate
def test_show_device_ignore_neverpoll(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    client.show_device(ignore_neverpoll=True)
    params = qs(responses.calls[0].request.url)
    assert params["ignore_neverpoll"] == ["True"]


@responses.activate
def test_show_device_negated_status(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    client.show_device(status=["!dead"])
    params = qs(responses.calls[0].request.url)
    assert params["status"] == ["!dead"]


@responses.activate
def test_show_device_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/device/show", json=DEVICE_SHOW)
    client.show_device()
    params = qs(responses.calls[0].request.url)
    assert "os" not in params
    assert "status" not in params
    assert "vendor" not in params


@responses.activate
def test_summarize_device(client):
    responses.add(responses.GET, f"{API}/device/summarize", json={})
    result = client.summarize_device()
    assert result == {}


@responses.activate
def test_unique_device(client):
    responses.add(responses.GET, f"{API}/device/unique", json=[])
    client.unique_device(what="os")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["os"]


@responses.activate
def test_top_device(client):
    responses.add(responses.GET, f"{API}/device/top", json=DEVICE_SHOW)
    client.top_device(what="version", count="10")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["version"]
    assert params["count"] == ["10"]
