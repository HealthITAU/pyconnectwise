from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyInfoServicesIdEndpoint import SystemMycompanyInfoServicesIdEndpoint
from pyconnectwise.models.manage import ServiceInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyInfoServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "services", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemMycompanyInfoServicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyInfoServicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyInfoServicesIdEndpoint: The initialized SystemMycompanyInfoServicesIdEndpoint object.
        """
        child = SystemMycompanyInfoServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceInfo]:
        """
        Performs a GET request against the /system/mycompany/info/services endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceInfo]:
        """
        Performs a GET request against the /system/mycompany/info/services endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceInfo]: The parsed response data.
        """
        return self._parse_many(ServiceInfo, super()._make_request("GET", data=data, params=params).json())
