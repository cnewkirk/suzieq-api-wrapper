"""Base HTTP client for the SuzieQ REST API."""
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from urllib3.util.retry import Retry

from ._exceptions import (
    BadRequestError, AuthenticationError, NotFoundError,
    ValidationError, ServerError, SuzieQHTTPError,
)


class _SuzieQBase:
    """Base class providing authenticated HTTP helpers."""

    def __init__(self, url: str, api_key: str,
                 verify_ssl: bool = True, timeout: int = 30,
                 retries: int = 3):
        """Initialize base URL, API key, and a shared requests session.

        Args:
            url: Base URL of the SuzieQ REST server
                (e.g. ``"https://127.0.0.1:8000"``).
            api_key: SuzieQ API key configured as ``rest.API_KEY`` in
                ``~/.suzieq/suzieq.cfg``.
            verify_ssl: When ``False`` SSL certificate verification is
                disabled.  Defaults to ``True``.  Set to ``False`` for
                self-signed certs in dev/test environments.
            timeout: Read timeout in seconds for all HTTP requests.
                The connect timeout is capped at ``min(timeout, 10)``
                seconds so unreachable hosts fail fast.
                Defaults to ``30``.  Pass ``None`` to disable.
            retries: Number of retries on connection errors and
                HTTP 500/502/503/504.  Uses exponential backoff with
                a 0.5 s factor.  Pass ``0`` to disable retries.
        """
        base = url.rstrip("/")
        self._base_url = f"{base}/api/v2"
        self._timeout = (
            (min(timeout, 10), timeout) if timeout is not None else None
        )
        self._session = requests.Session()
        self._session.headers.update({
            "Accept": "application/json",
            "access_token": api_key,
        })
        self._session.verify = verify_ssl
        retry = Retry(
            total=retries,
            backoff_factor=0.5,
            status_forcelist=(500, 502, 503, 504),
            allowed_methods=None,
            raise_on_status=False,
        ) if retries > 0 else 0
        adapter = HTTPAdapter(
            pool_connections=4, pool_maxsize=20, max_retries=retry
        )
        self._session.mount("https://", adapter)
        self._session.mount("http://", adapter)

    @staticmethod
    def _build_params(**kwargs) -> dict:
        """Return a params dict with ``None`` values stripped."""
        return {k: v for k, v in kwargs.items() if v is not None}

    def _url(self, table: str, verb: str) -> str:
        """Build a full endpoint URL for *table* and *verb*."""
        return f"{self._base_url}/{table}/{verb}"

    def _raise_for_status(self, resp: requests.Response) -> None:
        """Translate an HTTP error response into a library exception."""
        try:
            resp.raise_for_status()
        except HTTPError as exc:
            status = resp.status_code
            msg = str(exc)
            if status == 401:
                raise AuthenticationError(msg, resp) from exc
            if status == 404:
                raise NotFoundError(msg, resp) from exc
            if status == 405:
                raise BadRequestError(msg, resp) from exc
            if status == 422:
                raise ValidationError(msg, resp) from exc
            if 500 <= status < 600:
                raise ServerError(msg, resp) from exc
            raise SuzieQHTTPError(msg, resp) from exc

    def _parse(self, resp: requests.Response):
        """Parse an HTTP response into a Python object.

        Returns a list of dicts for ``show``/``unique``/``top``,
        a dict for ``summarize``, or raises a
        :class:`SuzieQHTTPError` subclass on non-2xx status codes.
        """
        self._raise_for_status(resp)
        if not resp.content:
            return None
        return resp.json()

    def _get(self, table: str, verb: str, params: dict = None):
        """Send a GET request to ``/api/v2/{table}/{verb}`` and return the
        parsed response.

        Args:
            table: SuzieQ table name (e.g. ``"bgp"``, ``"interface"``).
            verb: SuzieQ verb (e.g. ``"show"``, ``"summarize"``).
            params: Query parameters dict passed to ``requests``.

        Returns:
            Parsed JSON response — a list of dicts for most verbs, a
            column-oriented dict for ``summarize``.
        """
        resp = self._session.get(
            self._url(table, verb), params=params, timeout=self._timeout
        )
        return self._parse(resp)
