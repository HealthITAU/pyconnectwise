from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementCountEndpoint import CompanyManagementCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdEndpoint import CompanyManagementIdEndpoint
from pyconnectwise.models.manage import Management
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManagementEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "management", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyManagementCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyManagementIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementIdEndpoint: The initialized CompanyManagementIdEndpoint object.
        """
        child = CompanyManagementIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Management]:
        """
        Performs a GET request against the /company/management endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Management]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Management, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Management]:
        """
        Performs a GET request against the /company/management endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Management]: The parsed response data.
        """
        return self._parse_many(Management, super()._make_request("GET", data=data, params=params).json())
