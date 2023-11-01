from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechRouter
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class RoutersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechRouter], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechRouter, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Routers", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechRouter])
        IPaginateable.__init__(self, LabTechRouter)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechRouter]:
        """
        Performs a GET request against the /Routers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechRouter]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechRouter,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechRouter]:
        """
        Performs a GET request against the /Routers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechRouter]: The parsed response data.
        """
        return self._parse_many(
            LabTechRouter, super()._make_request("GET", data=data, params=params).json()
        )
