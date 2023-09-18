from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCrmCountEndpoint import SystemMycompanyCrmCountEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCrmIdEndpoint import SystemMycompanyCrmIdEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCrmInfoEndpoint import SystemMycompanyCrmInfoEndpoint
from pyconnectwise.models.manage import Crm
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyCrmEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "crm", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMycompanyCrmCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemMycompanyCrmInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMycompanyCrmIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyCrmIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyCrmIdEndpoint: The initialized SystemMycompanyCrmIdEndpoint object.
        """
        child = SystemMycompanyCrmIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Crm]:
        """
        Performs a GET request against the /system/myCompany/crm endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Crm]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Crm, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Crm]:
        """
        Performs a GET request against the /system/myCompany/crm endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Crm]: The parsed response data.
        """
        return self._parse_many(Crm, super()._make_request("GET", data=data, params=params).json())
