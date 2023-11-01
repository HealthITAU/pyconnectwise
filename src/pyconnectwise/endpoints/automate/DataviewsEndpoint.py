from typing import Any

from pyconnectwise.endpoints.automate.DataviewsIdEndpoint import DataviewsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.automate import LabTechDataView
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class DataviewsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechDataView], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechDataView, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Dataviews", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechDataView])
        IPaginateable.__init__(self, LabTechDataView)

    def id(self, id: int) -> DataviewsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized DataviewsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            DataviewsIdEndpoint: The initialized DataviewsIdEndpoint object.
        """
        child = DataviewsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechDataView]:
        """
        Performs a GET request against the /Dataviews endpoint and returns an initialized PaginatedResponse object.

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
    ) -> list[LabTechDataView]:
        """
        Performs a GET request against the /Dataviews endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechDataView]: The parsed response data.
        """
        return self._parse_many(
            LabTechDataView,
            super()._make_request("GET", data=data, params=params).json(),
        )
