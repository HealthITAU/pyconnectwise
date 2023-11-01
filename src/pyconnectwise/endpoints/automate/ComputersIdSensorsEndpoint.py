from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechComputerSensor
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ComputersIdSensorsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechComputerSensor], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechComputerSensor, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Sensors", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechComputerSensor])
        IPaginateable.__init__(self, LabTechComputerSensor)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechComputerSensor]:
        """
        Performs a GET request against the /Computers/{id}/Sensors endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerSensor]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechComputerSensor,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechComputerSensor]:
        """
        Performs a GET request against the /Computers/{id}/Sensors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerSensor]: The parsed response data.
        """
        return self._parse_many(
            LabTechComputerSensor,
            super()._make_request("GET", data=data, params=params).json(),
        )
