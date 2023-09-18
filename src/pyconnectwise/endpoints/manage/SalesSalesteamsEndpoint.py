from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesSalesteamsCountEndpoint import SalesSalesteamsCountEndpoint
from pyconnectwise.endpoints.manage.SalesSalesteamsIdEndpoint import SalesSalesteamsIdEndpoint
from pyconnectwise.models.manage import SalesTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesSalesteamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "salesTeams", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesSalesteamsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesSalesteamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesSalesteamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesSalesteamsIdEndpoint: The initialized SalesSalesteamsIdEndpoint object.
        """
        child = SalesSalesteamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SalesTeam]:
        """
        Performs a GET request against the /sales/salesTeams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesTeam]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), SalesTeam, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SalesTeam]:
        """
        Performs a GET request against the /sales/salesTeams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesTeam]: The parsed response data.
        """
        return self._parse_many(SalesTeam, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SalesTeam:
        """
        Performs a POST request against the /sales/salesTeams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesTeam: The parsed response data.
        """
        return self._parse_one(SalesTeam, super()._make_request("POST", data=data, params=params).json())
