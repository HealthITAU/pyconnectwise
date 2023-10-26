import json
from typing import ClassVar
from urllib.parse import urlsplit, urlunsplit

from requests import JSONDecodeError, Response


class ConnectWiseException(Exception):  # noqa: N818
    _code_explanation: ClassVar[str] = ""  # Ex: for 404 "Not Found"
    _error_suggestion: ClassVar[
        str
    ] = ""  # Ex: for 404 "Check the URL you are using is correct"

    def __init__(self, req_response: Response) -> None:
        self.response = req_response
        super().__init__(self.message())

    def _get_sanitized_url(self) -> str:
        """
        Simplify URL down to method, hostname, and path.
        """
        url_components = urlsplit(self.response.url)
        return urlunsplit(
            (
                url_components.scheme,
                url_components.hostname,
                url_components.path,
                "",
                "",
            )
        )

    def details(self) -> str:
        try:
            # If response was json, then format it nicely
            return json.dumps(self.response.json(), indent=4)
        except JSONDecodeError:
            return self.response.text

    def message(self) -> str:
        return (
            f"A HTTP {self.response.status_code} ({self._code_explanation}) error has occurred while requesting"
            f" {self._get_sanitized_url()}.\n{self.response.reason}\n{self._error_suggestion}"
        )


class MalformedRequestException(ConnectWiseException):
    _code_explanation = "Bad Request"
    _error_suggestion = (
        "The request could not be understood by the server due to malformed syntax. Please check modify your request"
        " before retrying."
    )


class AuthenticationFailedException(ConnectWiseException):
    _code_explanation = "Unauthorized"
    _error_suggestion = "Please check your credentials are correct before retrying."


class PermissionsFailedException(ConnectWiseException):
    _code_explanation = "Forbidden"
    _error_suggestion = "You may be attempting to access a resource you do not have the appropriate permissions for."


class NotFoundException(ConnectWiseException):
    _code_explanation = "Not Found"
    _error_suggestion = (
        "You may be attempting to access a resource that has been moved or deleted."
    )


class MethodNotAllowedException(ConnectWiseException):
    _code_explanation = "Method Not Allowed"
    _error_suggestion = (
        "This resource does not support the HTTP method you are trying to use."
    )


class ConflictException(ConnectWiseException):
    _code_explanation = "Conflict"
    _error_suggestion = (
        "This resource is possibly in use or conflicts with another record."
    )


class ServerError(ConnectWiseException):
    _code_explanation = "Internal Server Error"
