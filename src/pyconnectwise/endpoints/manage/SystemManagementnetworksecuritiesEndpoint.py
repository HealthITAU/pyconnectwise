from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemManagementnetworksecuritiesCountEndpoint import \
    SystemManagementnetworksecuritiesCountEndpoint
from pyconnectwise.endpoints.manage.SystemManagementnetworksecuritiesIdEndpoint import \
    SystemManagementnetworksecuritiesIdEndpoint
from pyconnectwise.models.manage import ManagementNetworkSecurity
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemManagementnetworksecuritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementNetworkSecurities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemManagementnetworksecuritiesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemManagementnetworksecuritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemManagementnetworksecuritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemManagementnetworksecuritiesIdEndpoint: The initialized SystemManagementnetworksecuritiesIdEndpoint object.
        """
        child = SystemManagementnetworksecuritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagementNetworkSecurity]:
        """
        Performs a GET request against the /system/managementNetworkSecurities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementNetworkSecurity]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagementNetworkSecurity, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementNetworkSecurity]:
        """
        Performs a GET request against the /system/managementNetworkSecurities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementNetworkSecurity]: The parsed response data.
        """
        return self._parse_many(
            ManagementNetworkSecurity, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementNetworkSecurity:
        """
        Performs a POST request against the /system/managementNetworkSecurities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementNetworkSecurity: The parsed response data.
        """
        return self._parse_one(
            ManagementNetworkSecurity, super()._make_request("POST", data=data, params=params).json()
        )
