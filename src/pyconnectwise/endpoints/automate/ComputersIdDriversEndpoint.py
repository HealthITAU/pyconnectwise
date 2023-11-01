from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechComputerDriver
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ComputersIdDriversEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechComputerDriver], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechComputerDriver, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Drivers", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechComputerDriver])
        IPaginateable.__init__(self, LabTechComputerDriver)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechComputerDriver]:
        """
        Performs a GET request against the /Computers/{id}/Drivers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerDriver]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechComputerDriver,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechComputerDriver]:
        """
        Performs a GET request against the /Computers/{id}/Drivers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerDriver]: The parsed response data.
        """
        return self._parse_many(
            LabTechComputerDriver,
            super()._make_request("GET", data=data, params=params).json(),
        )
