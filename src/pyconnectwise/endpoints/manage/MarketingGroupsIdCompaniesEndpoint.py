from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdCompaniesCountEndpoint import \
    MarketingGroupsIdCompaniesCountEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdCompaniesIdEndpoint import MarketingGroupsIdCompaniesIdEndpoint
from pyconnectwise.models.manage import MarketingCompany
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingGroupsIdCompaniesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companies", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingGroupsIdCompaniesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingGroupsIdCompaniesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingGroupsIdCompaniesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingGroupsIdCompaniesIdEndpoint: The initialized MarketingGroupsIdCompaniesIdEndpoint object.
        """
        child = MarketingGroupsIdCompaniesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MarketingCompany]:
        """
        Performs a GET request against the /marketing/groups/{id}/companies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MarketingCompany]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MarketingCompany, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MarketingCompany]:
        """
        Performs a GET request against the /marketing/groups/{id}/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MarketingCompany]: The parsed response data.
        """
        return self._parse_many(MarketingCompany, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MarketingCompany:
        """
        Performs a POST request against the /marketing/groups/{id}/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketingCompany: The parsed response data.
        """
        return self._parse_one(MarketingCompany, super()._make_request("POST", data=data, params=params).json())
