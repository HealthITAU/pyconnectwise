from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.automate import AutomateAuthInformation, AutomateTokenResult
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ApitokenEndpoint(
    ConnectWiseEndpoint,
    IGettable[AutomateAuthInformation, ConnectWiseAutomateRequestParams],
    IPostable[AutomateTokenResult, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Apitoken", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, AutomateAuthInformation)
        IPostable.__init__(self, AutomateTokenResult)

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateAuthInformation:
        """
        Performs a GET request against the /Apitoken endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateAuthInformation: The parsed response data.
        """
        return self._parse_one(
            AutomateAuthInformation,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateTokenResult:
        """
        Performs a POST request against the /Apitoken endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateTokenResult: The parsed response data.
        """
        return self._parse_one(
            AutomateTokenResult,
            super()._make_request("POST", data=data, params=params).json(),
        )
