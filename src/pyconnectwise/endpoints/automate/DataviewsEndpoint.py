from typing import Any

from pyconnectwise.endpoints.automate.DataviewsIdEndpoint import DataviewsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechDataView
from pyconnectwise.responses.paginated_response import PaginatedResponse


class DataviewsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Dataviews", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechDataView, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechDataView]:
        """
        Performs a GET request against the /Dataviews endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechDataView]: The parsed response data.
        """
        return self._parse_many(LabTechDataView, super()._make_request("GET", data=data, params=params).json())
