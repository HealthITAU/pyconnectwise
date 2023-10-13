from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import AutomateUserClassWebExtensionViewModel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class UserclassesIdWebextensionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateUserClassWebExtensionViewModel], ConnectWiseAutomateRequestParams],
    IPuttable[list[AutomateUserClassWebExtensionViewModel], ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Webextensions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[AutomateUserClassWebExtensionViewModel])
        IPuttable.__init__(self, list[AutomateUserClassWebExtensionViewModel])

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[AutomateUserClassWebExtensionViewModel]:
        """
        Performs a GET request against the /Userclasses/{id}/Webextensions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateUserClassWebExtensionViewModel]: The parsed response data.
        """
        return self._parse_many(
            AutomateUserClassWebExtensionViewModel, super()._make_request("GET", data=data, params=params).json()
        )

    def put(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[AutomateUserClassWebExtensionViewModel]:
        """
        Performs a PUT request against the /Userclasses/{id}/Webextensions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateUserClassWebExtensionViewModel]: The parsed response data.
        """
        return self._parse_many(
            AutomateUserClassWebExtensionViewModel, super()._make_request("PUT", data=data, params=params).json()
        )
