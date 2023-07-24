from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.Automate.Api.Domain.Contracts.PresentationLayer.WebExtensions import \
    UserClassWebExtensionViewModel
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class UserclassesIdWebextensionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Webextensions", parent_endpoint=parent_endpoint)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UserClassWebExtensionViewModel]:
        """
        Performs a GET request against the /Userclasses/{id}/Webextensions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UserClassWebExtensionViewModel]: The parsed response data.
        """
        return self._parse_many(
            UserClassWebExtensionViewModel, super()._make_request("GET", data=data, params=params).json()
        )

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UserClassWebExtensionViewModel]:
        """
        Performs a PUT request against the /Userclasses/{id}/Webextensions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UserClassWebExtensionViewModel]: The parsed response data.
        """
        return self._parse_many(
            UserClassWebExtensionViewModel, super()._make_request("PUT", data=data, params=params).json()
        )
