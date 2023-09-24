from __future__ import annotations
from typing import Any, cast
import requests
from requests import Response
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from pyconnectwise.exceptions import *
import pyconnectwise.config as config
from abc import ABC, abstractmethod
from pyconnectwise.config import Config
from pyconnectwise.types import (
    JSON,
    Patch,
    PatchRequestData,
    RequestData,
    ConnectWiseManageRequestParams,
    RequestMethod,
    GenericRequestParams,
    RequestParams,
)


class ConnectWiseClient(ABC):
    config: Config = Config()

    @abstractmethod
    def _get_headers(self) -> dict[str, str]:
        pass

    @abstractmethod
    def _get_url(self) -> str:
        pass

    def _make_request(
        self,
        method: RequestMethod,
        url: str,
        data: RequestData | None = None,
        params: RequestParams | None = None,
        headers: dict[str, str] | None = None,
        retry_count: int = 0,
    ) -> Response:
        """
        Make an API request using the specified method, endpoint, data, and parameters.
        This function isn't intended for use outside of this class.
        Please use the available CRUD methods as intended.

        Args:
            method (str): The HTTP method to use for the request (e.g., GET, POST, PUT, etc.).
            endpoint (str, optional): The endpoint to make the request to.
            data (dict, optional): The request data to send.
            params (dict, optional): The query parameters to include in the request.

        Returns:
            The Response object (see requests.Response).

        Raises:
            Exception: If the request returns a status code >= 400.
        """

        if not headers:
            headers = self._get_headers()

        # I don't like having to cast the params to a dict, but it's the only way I can get mypy to stop complaining about the type.
        # TypedDicts aren't compatible with the dict type and this is the best way I can think of to handle this.
        if data:
            response = requests.request(
                method,
                url,
                headers=headers,
                json=data,
                params=cast(dict[str, Any], params or {}),
            )
        else:
            response = requests.request(
                method,
                url,
                headers=headers,
                params=cast(dict[str, Any], params or {}),
            )
        try:
            response.raise_for_status()
        except HTTPError as http_error:
            msg = str(http_error)
            if response.status_code == 400:
                raise MalformedRequestException(msg) from http_error
            if response.status_code == 401:
                raise AuthenticationFailedException(msg) from http_error
            if response.status_code == 403:
                raise PermissionsFailedException(msg) from http_error
            if response.status_code == 404:
                raise NotFoundException(msg) from http_error
            if response.status_code == 405:
                raise MethodNotAllowedException(msg) from http_error
            if response.status_code == 409:
                raise ConflictException(msg) from http_error
            if response.status_code == 500:
                if retry_count < self.config.max_retries:
                    retry_count += 1
                    return self._make_request(
                        method, url, data, params, headers, retry_count
                    )
            else:
                raise http_error
        except Timeout as timeout_error:
            raise timeout_error
        except ConnectionError as conn_error:
            raise conn_error
        except RequestException as req_error:
            raise req_error

        return response
