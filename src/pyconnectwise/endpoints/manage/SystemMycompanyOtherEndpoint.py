from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyOtherCountEndpoint import SystemMycompanyOtherCountEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyOtherIdEndpoint import SystemMycompanyOtherIdEndpoint
from pyconnectwise.models.manage import Other
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyOtherEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "other", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMycompanyOtherCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMycompanyOtherIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyOtherIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyOtherIdEndpoint: The initialized SystemMycompanyOtherIdEndpoint object.
        """
        child = SystemMycompanyOtherIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Other]:
        """
        Performs a GET request against the /system/myCompany/other endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Other]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Other, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Other]:
        """
        Performs a GET request against the /system/myCompany/other endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Other]: The parsed response data.
        """
        return self._parse_many(Other, super()._make_request("GET", data=data, params=params).json())
