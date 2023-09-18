from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyServicesIdEndpoint import SystemMycompanyServicesIdEndpoint
from pyconnectwise.models.manage import Service
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "services", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemMycompanyServicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyServicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyServicesIdEndpoint: The initialized SystemMycompanyServicesIdEndpoint object.
        """
        child = SystemMycompanyServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Service]:
        """
        Performs a GET request against the /system/mycompany/services endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Service]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Service, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Service]:
        """
        Performs a GET request against the /system/mycompany/services endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Service]: The parsed response data.
        """
        return self._parse_many(Service, super()._make_request("GET", data=data, params=params).json())
