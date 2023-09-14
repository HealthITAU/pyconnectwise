from __future__ import annotations
from typing import Any
import requests
from requests import Response
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from pyconnectwise.exceptions import *
import pyconnectwise.config as config
from abc import ABC, abstractmethod
from pyconnectwise.config import Config


class ConnectWiseClient(ABC):
    config: Config = Config()

    @abstractmethod
    def _get_headers(self) -> dict[str, str]:
        pass

    def _make_request(
            self,
            method: str,
            url: str,
            data: dict[str, Any] = None,
            params: dict[str, int | str] = None,
            headers: dict[str, str] = None,
            retry_count: int = 0
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
        if not params:
            params = {}

        if not headers:
            headers = self._get_headers()

        if data:
            response = requests.request(
                method, url, headers=headers, json=data, params=params
            )
        else:
            response = requests.request(
                method, url, headers=headers, params=params
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
                    return self._make_request(method, url, data, params, headers, retry_count)
            else:
                raise http_error
        except Timeout as timeout_error:
            raise timeout_error
        except ConnectionError as conn_error:
            raise conn_error
        except RequestException as req_error:
            raise req_error

        return response
