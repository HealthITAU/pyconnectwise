from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementbackupsCountEndpoint import CompanyManagementbackupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementbackupsIdEndpoint import CompanyManagementbackupsIdEndpoint
from pyconnectwise.models.manage import ManagementBackup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManagementbackupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementBackups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyManagementbackupsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyManagementbackupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementbackupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementbackupsIdEndpoint: The initialized CompanyManagementbackupsIdEndpoint object.
        """
        child = CompanyManagementbackupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagementBackup]:
        """
        Performs a GET request against the /company/managementBackups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementBackup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagementBackup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementBackup]:
        """
        Performs a GET request against the /company/managementBackups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementBackup]: The parsed response data.
        """
        return self._parse_many(ManagementBackup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementBackup:
        """
        Performs a POST request against the /company/managementBackups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementBackup: The parsed response data.
        """
        return self._parse_one(ManagementBackup, super()._make_request("POST", data=data, params=params).json())
