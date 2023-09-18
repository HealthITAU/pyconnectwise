from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesCountEndpoint import ServicePrioritiesCountEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesIdEndpoint import ServicePrioritiesIdEndpoint
from pyconnectwise.models.manage import Priority
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServicePrioritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "priorities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServicePrioritiesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServicePrioritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServicePrioritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServicePrioritiesIdEndpoint: The initialized ServicePrioritiesIdEndpoint object.
        """
        child = ServicePrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Priority]:
        """
        Performs a GET request against the /service/priorities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Priority]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Priority, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Priority]:
        """
        Performs a GET request against the /service/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Priority]: The parsed response data.
        """
        return self._parse_many(Priority, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Priority:
        """
        Performs a POST request against the /service/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Priority: The parsed response data.
        """
        return self._parse_one(Priority, super()._make_request("POST", data=data, params=params).json())
