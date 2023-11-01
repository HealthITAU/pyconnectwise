from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechSensorCheck
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class SensorchecksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechSensorCheck], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechSensorCheck, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Sensorchecks", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechSensorCheck])
        IPaginateable.__init__(self, LabTechSensorCheck)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechSensorCheck]:
        """
        Performs a GET request against the /Sensorchecks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechSensorCheck]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechSensorCheck,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechSensorCheck]:
        """
        Performs a GET request against the /Sensorchecks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechSensorCheck]: The parsed response data.
        """
        return self._parse_many(
            LabTechSensorCheck,
            super()._make_request("GET", data=data, params=params).json(),
        )
