"""Exception hierarchy for suzieq-api-wrapper."""


class SuzieQError(Exception):
    """Base class for all suzieq-api-wrapper exceptions."""


class SuzieQHTTPError(SuzieQError):
    """Raised when the SuzieQ server returns an HTTP error response.

    Attributes:
        status_code: The HTTP status code returned by the server.
        response: The original ``requests.Response`` object, providing
            access to headers, URL, and raw body.
    """

    def __init__(self, message: str, response=None):
        super().__init__(message)
        self.response = response
        self.status_code = response.status_code if response is not None else None


class AuthenticationError(SuzieQHTTPError):
    """401 Unauthorized — API key is missing or invalid."""


class NotFoundError(SuzieQHTTPError):
    """404 Not Found — unknown table, verb, or attribute."""


class BadRequestError(SuzieQHTTPError):
    """405 Method Not Allowed — unsupported query parameter or value."""


class ValidationError(SuzieQHTTPError):
    """422 Unprocessable Entity — FastAPI parameter validation failed."""


class ServerError(SuzieQHTTPError):
    """5xx Server Error — the SuzieQ server encountered an internal error."""
