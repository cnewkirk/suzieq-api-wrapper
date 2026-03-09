"""Tests for _SuzieQBase – session setup, error handling, _parse, _build_params."""
import pytest
import responses

import suzieq_api_wrapper as suzieq
from suzieq_api_wrapper._base import _SuzieQBase
from suzieq_api_wrapper._exceptions import (
    AuthenticationError,
    BadRequestError,
    NotFoundError,
    ServerError,
    SuzieQHTTPError,
    ValidationError,
)
from .conftest import API, BASE_URL


# ── _build_params ──────────────────────────────────────────────────────────


class TestBuildParams:
    def test_strips_none_values(self):
        result = _SuzieQBase._build_params(a="x", b=None, c="z")
        assert result == {"a": "x", "c": "z"}

    def test_all_none_returns_empty(self):
        result = _SuzieQBase._build_params(a=None, b=None)
        assert result == {}

    def test_no_args_returns_empty(self):
        result = _SuzieQBase._build_params()
        assert result == {}

    def test_preserves_non_none_values(self):
        result = _SuzieQBase._build_params(
            namespace=["dc1"], hostname=["leaf01"], state="up"
        )
        assert result == {
            "namespace": ["dc1"],
            "hostname": ["leaf01"],
            "state": "up",
        }

    def test_preserves_lists(self):
        result = _SuzieQBase._build_params(
            columns=["hostname", "state", "peer"]
        )
        assert result == {"columns": ["hostname", "state", "peer"]}

    def test_preserves_false_and_zero(self):
        result = _SuzieQBase._build_params(a=False, b=0, c="")
        assert result == {"a": False, "b": 0, "c": ""}


# ── Session setup ──────────────────────────────────────────────────────────


class TestSessionSetup:
    def test_api_key_in_header(self, client):
        assert client._session.headers["access_token"] == "test-api-key"

    def test_accept_header(self, client):
        assert client._session.headers["Accept"] == "application/json"

    def test_verify_ssl_true_default(self):
        c = suzieq.SuzieQ("https://example.com", "key")
        assert c._session.verify is True

    def test_verify_ssl_false(self):
        c = suzieq.SuzieQ("https://example.com", "key", verify_ssl=False)
        assert c._session.verify is False

    def test_base_url(self, client):
        assert client._base_url == f"{BASE_URL}/api/v2"

    def test_base_url_trailing_slash_stripped(self):
        c = suzieq.SuzieQ("http://host:8000/", "key")
        assert c._base_url == "http://host:8000/api/v2"

    def test_timeout_tuple(self, client):
        assert client._timeout == (10, 30)

    def test_timeout_short(self):
        c = suzieq.SuzieQ("http://h", "k", timeout=5)
        assert c._timeout == (5, 5)

    def test_timeout_none(self):
        c = suzieq.SuzieQ("http://h", "k", timeout=None)
        assert c._timeout is None

    def test_retry_adapter_mounted(self, client):
        adapter = client._session.get_adapter("https://example.com")
        assert adapter.max_retries.total == 3

    def test_retries_disabled(self):
        c = suzieq.SuzieQ("http://h", "k", retries=0)
        adapter = c._session.get_adapter("https://example.com")
        assert adapter.max_retries.total == 0


# ── URL building ───────────────────────────────────────────────────────────


class TestUrlBuilding:
    def test_url_basic(self, client):
        assert client._url("bgp", "show") == f"{API}/bgp/show"

    def test_url_camelCase_table(self, client):
        assert client._url("evpnVni", "assert") == f"{API}/evpnVni/assert"

    def test_url_with_verb(self, client):
        assert client._url("route", "lpm") == f"{API}/route/lpm"


# ── _parse / _raise_for_status / error handling ───────────────────────────


class TestParse:
    @responses.activate
    def test_json_response(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            json=[{"state": "Established"}],
        )
        result = client._get("bgp", "show")
        assert result == [{"state": "Established"}]

    @responses.activate
    def test_empty_body_returns_none(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            body="", status=204,
        )
        result = client._get("bgp", "show")
        assert result is None


class TestErrorHandling:
    @responses.activate
    def test_401_raises_authentication_error(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            json={"error": "invalid key"}, status=401,
        )
        with pytest.raises(AuthenticationError) as exc_info:
            client._get("bgp", "show")
        assert exc_info.value.status_code == 401
        assert exc_info.value.response is not None

    @responses.activate
    def test_404_raises_not_found_error(self, client):
        responses.add(
            responses.GET, f"{API}/invalid/show",
            json={"error": "not found"}, status=404,
        )
        with pytest.raises(NotFoundError) as exc_info:
            client._get("invalid", "show")
        assert exc_info.value.status_code == 404

    @responses.activate
    def test_405_raises_bad_request_error(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            json={"error": "bad param"}, status=405,
        )
        with pytest.raises(BadRequestError) as exc_info:
            client._get("bgp", "show")
        assert exc_info.value.status_code == 405

    @responses.activate
    def test_422_raises_validation_error(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            json={"detail": "validation error"}, status=422,
        )
        with pytest.raises(ValidationError) as exc_info:
            client._get("bgp", "show")
        assert exc_info.value.status_code == 422

    @responses.activate
    def test_500_raises_server_error(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            json={"error": "internal"}, status=500,
        )
        with pytest.raises(ServerError) as exc_info:
            client._get("bgp", "show")
        assert exc_info.value.status_code == 500

    @responses.activate
    def test_502_raises_server_error(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            body="bad gateway", status=502,
        )
        with pytest.raises(ServerError) as exc_info:
            client._get("bgp", "show")
        assert exc_info.value.status_code == 502

    @responses.activate
    def test_418_raises_generic_http_error(self, client):
        responses.add(
            responses.GET, f"{API}/bgp/show",
            body="teapot", status=418,
        )
        with pytest.raises(SuzieQHTTPError) as exc_info:
            client._get("bgp", "show")
        assert exc_info.value.status_code == 418
        assert not isinstance(exc_info.value, AuthenticationError)
        assert not isinstance(exc_info.value, ServerError)


# ── Exception hierarchy ───────────────────────────────────────────────────


class TestExceptionHierarchy:
    def test_suzieq_http_error_is_suzieq_error(self):
        assert issubclass(SuzieQHTTPError, suzieq.SuzieQError)

    def test_authentication_error_is_http_error(self):
        assert issubclass(AuthenticationError, SuzieQHTTPError)

    def test_not_found_error_is_http_error(self):
        assert issubclass(NotFoundError, SuzieQHTTPError)

    def test_bad_request_error_is_http_error(self):
        assert issubclass(BadRequestError, SuzieQHTTPError)

    def test_validation_error_is_http_error(self):
        assert issubclass(ValidationError, SuzieQHTTPError)

    def test_server_error_is_http_error(self):
        assert issubclass(ServerError, SuzieQHTTPError)

    def test_http_error_preserves_response(self):
        exc = SuzieQHTTPError("test", None)
        assert exc.response is None
        assert exc.status_code is None

    def test_all_catchable_via_base(self):
        """All typed errors can be caught with ``except SuzieQError``."""
        for cls in (AuthenticationError, NotFoundError, BadRequestError,
                    ValidationError, ServerError, SuzieQHTTPError):
            assert issubclass(cls, suzieq.SuzieQError)


# ── _get integration ──────────────────────────────────────────────────────


class TestGetIntegration:
    @responses.activate
    def test_get_sends_auth_header(self, client):
        responses.add(responses.GET, f"{API}/device/show", json=[])
        client._get("device", "show")
        assert responses.calls[0].request.headers["access_token"] == "test-api-key"

    @responses.activate
    def test_get_sends_params(self, client):
        responses.add(responses.GET, f"{API}/bgp/show", json=[])
        client._get("bgp", "show", params={"state": "Established"})
        assert "state=Established" in responses.calls[0].request.url

    @responses.activate
    def test_get_list_params_repeat(self, client):
        responses.add(responses.GET, f"{API}/bgp/show", json=[])
        client._get("bgp", "show", params={"namespace": ["dc1", "dc2"]})
        url = responses.calls[0].request.url
        assert "namespace=dc1" in url
        assert "namespace=dc2" in url

    @responses.activate
    def test_get_no_params(self, client):
        responses.add(responses.GET, f"{API}/bgp/show", json=[])
        client._get("bgp", "show")
        assert "?" not in responses.calls[0].request.url
