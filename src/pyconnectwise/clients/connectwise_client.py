from __future__ import annotations

import contextlib
import json
import warnings
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, cast

import requests
from requests import Response
from requests.exceptions import Timeout

from pyconnectwise.config import Config
from pyconnectwise.exceptions import (
    AuthenticationFailedException,
    ConflictException,
    MalformedRequestException,
    MethodNotAllowedException,
    NotFoundException,
    ObjectExistsError,
    PermissionsFailedException,
    ServerError,
)

if TYPE_CHECKING:
    from pyconnectwise.types import RequestData, RequestMethod, RequestParams


class ConnectWiseClient(ABC):
    config: Config = Config()

    @abstractmethod
    def _get_headers(self) -> dict[str, str]:
        pass

    @abstractmethod
    def _get_cookies(self) -> dict[str, str]:
        return {}

    @abstractmethod
    def _get_url(self) -> str:
        pass

    def _make_request(  # noqa: C901
        self,
        method: RequestMethod,
        url: str,
        data: RequestData | None = None,
        params: RequestParams | None = None,
        headers: dict[str, str] | None = None,
        retry_count: int = 0,
        stream: bool = False,  # noqa: FBT001, FBT002
        cookies: dict[str, str] | None = None,
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

        if not cookies:
            cookies = self._get_cookies()

        # I don't like having to cast the params to a dict, but it's the only way I can get mypy to stop complaining about the type.
        # TypedDicts aren't compatible with the dict type and this is the best way I can think of to handle this.
        if data:
            response = requests.request(  # noqa: S113
                method,
                url,
                headers=headers,
                json=data,
                params=cast(dict[str, Any], params or {}),
                stream=stream,
                cookies=cookies,
            )
        else:
            response = requests.request(  # noqa: S113
                method,
                url,
                headers=headers,
                params=cast(dict[str, Any], params or {}),
                stream=stream,
                cookies=cookies,
            )
        if not response.ok:
            with contextlib.suppress(json.JSONDecodeError):
                details: dict = response.json()
                if response.status_code == 400:  # noqa: SIM102 (Expecting to handle other codes in the future)
                    if details.get("code") == "InvalidObject":
                        errors = details.get("errors", [])
                        if len(errors) > 1:
                            warnings.warn(
                                "Found multiple errors - we may be masking some important error details.  Please submit a Github issue with response.status_code and response.content so we can improve this error handling.",
                                stacklevel=1,
                            )
                        for error in errors:
                            if error.get("code") == "ObjectExists":
                                error.pop("code")  # Don't need code in message
                                raise ObjectExistsError(response, extra_message=json.dumps(error, indent=4))

            if response.status_code == 400:
                raise MalformedRequestException(response)
            if response.status_code == 401:
                # TODO - Figure out a better way to retry on 401 if an authorization cookie is provided
                if retry_count < self.config.max_retries and "changeapproval" in cookies:
                    cookies["changeapproval"] = response.cookies["changeapproval"]
                    retry_count += 1
                    return self._make_request(method, url, data, params, headers, retry_count, cookies=cookies)
                raise AuthenticationFailedException(response)
            if response.status_code == 403:
                raise PermissionsFailedException(response)
            if response.status_code == 404:
                raise NotFoundException(response)
            if response.status_code == 405:
                raise MethodNotAllowedException(response)
            if response.status_code == 409:
                raise ConflictException(response)
            if response.status_code == 500:
                # if timeout is mentioned anywhere in the response then we'll retry.
                # Ideally we'd return immediately on any non-timeout errors (since
                # retries won't help much there), but err towards classifying too much
                # as retries instead of too little.
                if "timeout" in (response.text + response.reason).lower():
                    if retry_count < self.config.max_retries:
                        retry_count += 1
                        return self._make_request(method, url, data, params, headers, retry_count)
                    raise Timeout(response=response)
                raise ServerError(response)

        return response
