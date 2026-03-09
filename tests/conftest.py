"""Shared pytest fixtures and helpers."""
from urllib.parse import urlparse, parse_qs

import pytest
import suzieq_api_wrapper as suzieq

BASE_URL = "http://suzieq:8000"
API = f"{BASE_URL}/api/v2"
API_KEY = "test-api-key"


@pytest.fixture
def client():
    return suzieq.SuzieQ(BASE_URL, API_KEY, verify_ssl=False)


def qs(url: str) -> dict:
    """Parse query string from *url* into ``{key: [value, ...]}``."""
    return parse_qs(urlparse(url).query)
