"""Tests for EvpnVniMixin – /api/v2/evpnVni."""
import responses

from .conftest import API, qs
from .fixtures import EVPNVNI_SHOW, EVPNVNI_ASSERT


@responses.activate
def test_show_evpnvni_no_filters(client):
    responses.add(responses.GET, f"{API}/evpnVni/show", json=EVPNVNI_SHOW)
    result = client.show_evpnvni()
    assert result == EVPNVNI_SHOW
    assert responses.calls[0].request.headers["access_token"] == "test-api-key"


@responses.activate
def test_show_evpnvni_vni_filter(client):
    responses.add(responses.GET, f"{API}/evpnVni/show", json=EVPNVNI_SHOW)
    client.show_evpnvni(vni=["10100"])
    params = qs(responses.calls[0].request.url)
    assert params["vni"] == ["10100"]


@responses.activate
def test_show_evpnvni_priVtepIp_filter(client):
    responses.add(responses.GET, f"{API}/evpnVni/show", json=EVPNVNI_SHOW)
    client.show_evpnvni(priVtepIp=["10.0.1.1"])
    params = qs(responses.calls[0].request.url)
    assert params["priVtepIp"] == ["10.0.1.1"]


@responses.activate
def test_show_evpnvni_none_params_omitted(client):
    responses.add(responses.GET, f"{API}/evpnVni/show", json=EVPNVNI_SHOW)
    client.show_evpnvni()
    params = qs(responses.calls[0].request.url)
    assert "vni" not in params
    assert "priVtepIp" not in params


@responses.activate
def test_summarize_evpnvni(client):
    responses.add(responses.GET, f"{API}/evpnVni/summarize", json={})
    result = client.summarize_evpnvni()
    assert result == {}


@responses.activate
def test_unique_evpnvni(client):
    responses.add(responses.GET, f"{API}/evpnVni/unique", json=[])
    client.unique_evpnvni(what="vni")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["vni"]


@responses.activate
def test_top_evpnvni(client):
    responses.add(responses.GET, f"{API}/evpnVni/top", json=EVPNVNI_SHOW)
    client.top_evpnvni(what="vni", count="5")
    params = qs(responses.calls[0].request.url)
    assert params["what"] == ["vni"]
    assert params["count"] == ["5"]


@responses.activate
def test_assert_evpnvni_all(client):
    responses.add(responses.GET, f"{API}/evpnVni/assert", json=EVPNVNI_ASSERT)
    result = client.assert_evpnvni()
    assert result == EVPNVNI_ASSERT


@responses.activate
def test_assert_evpnvni_fail_only(client):
    responses.add(responses.GET, f"{API}/evpnVni/assert", json=[])
    client.assert_evpnvni(result="fail")
    params = qs(responses.calls[0].request.url)
    assert params["result"] == ["fail"]


@responses.activate
def test_assert_evpnvni_vni_filter(client):
    responses.add(responses.GET, f"{API}/evpnVni/assert", json=EVPNVNI_ASSERT)
    client.assert_evpnvni(vni=["10100"])
    params = qs(responses.calls[0].request.url)
    assert params["vni"] == ["10100"]
