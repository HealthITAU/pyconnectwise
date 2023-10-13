from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechComputerChassis
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ComputersChassisEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechComputerChassis], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechComputerChassis, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Chassis", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechComputerChassis])
        IPaginateable.__init__(self, LabTechComputerChassis)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechComputerChassis]:
        """
        Performs a GET request against the /Computers/Chassis endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerChassis]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechComputerChassis, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechComputerChassis]:
        """
        Performs a GET request against the /Computers/Chassis endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerChassis]: The parsed response data.
        """
        return self._parse_many(LabTechComputerChassis, super()._make_request("GET", data=data, params=params).json())
