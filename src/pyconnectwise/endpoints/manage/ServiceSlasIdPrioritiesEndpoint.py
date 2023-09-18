from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdPrioritiesCountEndpoint import ServiceSlasIdPrioritiesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdPrioritiesIdEndpoint import ServiceSlasIdPrioritiesIdEndpoint
from pyconnectwise.models.manage import SLAPriority
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSlasIdPrioritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "priorities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceSlasIdPrioritiesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSlasIdPrioritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSlasIdPrioritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSlasIdPrioritiesIdEndpoint: The initialized ServiceSlasIdPrioritiesIdEndpoint object.
        """
        child = ServiceSlasIdPrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SLAPriority]:
        """
        Performs a GET request against the /service/SLAs/{id}/priorities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SLAPriority]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SLAPriority, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SLAPriority]:
        """
        Performs a GET request against the /service/SLAs/{id}/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SLAPriority]: The parsed response data.
        """
        return self._parse_many(SLAPriority, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SLAPriority:
        """
        Performs a POST request against the /service/SLAs/{id}/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SLAPriority: The parsed response data.
        """
        return self._parse_one(SLAPriority, super()._make_request("POST", data=data, params=params).json())
