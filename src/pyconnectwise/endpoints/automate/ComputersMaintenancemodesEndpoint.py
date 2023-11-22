from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechMaintenanceMode
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ComputersMaintenancemodesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechMaintenanceMode], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechMaintenanceMode, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Maintenancemodes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechMaintenanceMode])
        IPaginateable.__init__(self, LabTechMaintenanceMode)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechMaintenanceMode]:
        """
        Performs a GET request against the /Computers/Maintenancemodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechMaintenanceMode]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechMaintenanceMode,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechMaintenanceMode]:
        """
        Performs a GET request against the /Computers/Maintenancemodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechMaintenanceMode]: The parsed response data.
        """
        return self._parse_many(
            LabTechMaintenanceMode,
            super()._make_request("GET", data=data, params=params).json(),
        )
