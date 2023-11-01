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
from pyconnectwise.models.automate import LabTechComputerMenu
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ComputermenusEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechComputerMenu], ConnectWiseAutomateRequestParams],
    IPostable[LabTechComputerMenu, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechComputerMenu, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Computermenus", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechComputerMenu])
        IPostable.__init__(self, LabTechComputerMenu)
        IPaginateable.__init__(self, LabTechComputerMenu)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechComputerMenu]:
        """
        Performs a GET request against the /Computermenus endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerMenu]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechComputerMenu,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechComputerMenu]:
        """
        Performs a GET request against the /Computermenus endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerMenu]: The parsed response data.
        """
        return self._parse_many(
            LabTechComputerMenu,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechComputerMenu:
        """
        Performs a POST request against the /Computermenus endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechComputerMenu: The parsed response data.
        """
        return self._parse_one(
            LabTechComputerMenu,
            super()._make_request("POST", data=data, params=params).json(),
        )
