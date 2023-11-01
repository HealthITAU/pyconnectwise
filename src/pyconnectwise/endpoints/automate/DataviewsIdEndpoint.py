from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechDataView
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class DataviewsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechDataView, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechDataView, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, LabTechDataView)
        IPaginateable.__init__(self, LabTechDataView)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechDataView]:
        """
        Performs a GET request against the /Dataviews/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechDataView]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechDataView,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechDataView:
        """
        Performs a GET request against the /Dataviews/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechDataView: The parsed response data.
        """
        return self._parse_one(
            LabTechDataView,
            super()._make_request("GET", data=data, params=params).json(),
        )
