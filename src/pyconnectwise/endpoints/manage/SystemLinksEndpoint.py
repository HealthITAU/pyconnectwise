from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLinksCountEndpoint import SystemLinksCountEndpoint
from pyconnectwise.endpoints.manage.SystemLinksIdEndpoint import SystemLinksIdEndpoint
from pyconnectwise.models.manage import Link
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "links", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemLinksCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemLinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLinksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLinksIdEndpoint: The initialized SystemLinksIdEndpoint object.
        """
        child = SystemLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Link]:
        """
        Performs a GET request against the /system/links endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Link]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Link, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Link]:
        """
        Performs a GET request against the /system/links endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Link]: The parsed response data.
        """
        return self._parse_many(Link, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Link:
        """
        Performs a POST request against the /system/links endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Link: The parsed response data.
        """
        return self._parse_one(Link, super()._make_request("POST", data=data, params=params).json())
