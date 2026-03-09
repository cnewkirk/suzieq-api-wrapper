"""suzieq_api_wrapper – a thin Python wrapper for the SuzieQ REST API."""
from .client import SuzieQ
from ._exceptions import (
    SuzieQError,
    SuzieQHTTPError,
    AuthenticationError,
    NotFoundError,
    BadRequestError,
    ValidationError,
    ServerError,
)
from importlib.metadata import version, PackageNotFoundError

__all__ = [
    "SuzieQ",
    "SuzieQError",
    "SuzieQHTTPError",
    "AuthenticationError",
    "NotFoundError",
    "BadRequestError",
    "ValidationError",
    "ServerError",
]

try:
    __version__ = version("suzieq-api-wrapper")
except PackageNotFoundError:
    __version__ = "unknown"
