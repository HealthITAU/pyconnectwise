from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdSoftwareIdEndpoint import ComputersIdSoftwareIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechComputerSoftware
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ComputersIdSoftwareEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechComputerSoftware], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechComputerSoftware, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Software", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechComputerSoftware])
        IPaginateable.__init__(self, LabTechComputerSoftware)

    def id(self, id: int) -> ComputersIdSoftwareIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ComputersIdSoftwareIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ComputersIdSoftwareIdEndpoint: The initialized ComputersIdSoftwareIdEndpoint object.
        """
        child = ComputersIdSoftwareIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechComputerSoftware]:
        """
        Performs a GET request against the /Computers/{id}/Software endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerSoftware]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechComputerSoftware, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechComputerSoftware]:
        """
        Performs a GET request against the /Computers/{id}/Software endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerSoftware]: The parsed response data.
        """
        return self._parse_many(LabTechComputerSoftware, super()._make_request("GET", data=data, params=params).json())
