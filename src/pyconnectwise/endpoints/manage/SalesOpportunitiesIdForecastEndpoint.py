from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastCopyEndpoint import \
    SalesOpportunitiesIdForecastCopyEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastCountEndpoint import \
    SalesOpportunitiesIdForecastCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastIdEndpoint import SalesOpportunitiesIdForecastIdEndpoint
from pyconnectwise.models.manage import Forecast
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesIdForecastEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "forecast", parent_endpoint=parent_endpoint)

        self.copy = self._register_child_endpoint(
            SalesOpportunitiesIdForecastCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(
            SalesOpportunitiesIdForecastCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOpportunitiesIdForecastIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdForecastIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdForecastIdEndpoint: The initialized SalesOpportunitiesIdForecastIdEndpoint object.
        """
        child = SalesOpportunitiesIdForecastIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Forecast]:
        """
        Performs a GET request against the /sales/opportunities/{id}/forecast endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Forecast]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Forecast, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Forecast]:
        """
        Performs a GET request against the /sales/opportunities/{id}/forecast endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Forecast]: The parsed response data.
        """
        return self._parse_many(Forecast, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Forecast:
        """
        Performs a POST request against the /sales/opportunities/{id}/forecast endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Forecast: The parsed response data.
        """
        return self._parse_one(Forecast, super()._make_request("POST", data=data, params=params).json())
