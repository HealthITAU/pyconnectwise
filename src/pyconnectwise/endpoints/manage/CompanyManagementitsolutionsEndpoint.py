from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsCountEndpoint import \
    CompanyManagementitsolutionsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsIdEndpoint import CompanyManagementitsolutionsIdEndpoint
from pyconnectwise.models.manage import ManagementItSolution
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManagementitsolutionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementItSolutions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyManagementitsolutionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyManagementitsolutionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementitsolutionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementitsolutionsIdEndpoint: The initialized CompanyManagementitsolutionsIdEndpoint object.
        """
        child = CompanyManagementitsolutionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagementItSolution]:
        """
        Performs a GET request against the /company/managementItSolutions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementItSolution]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagementItSolution, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementItSolution]:
        """
        Performs a GET request against the /company/managementItSolutions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementItSolution]: The parsed response data.
        """
        return self._parse_many(ManagementItSolution, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementItSolution:
        """
        Performs a POST request against the /company/managementItSolutions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolution: The parsed response data.
        """
        return self._parse_one(ManagementItSolution, super()._make_request("POST", data=data, params=params).json())
