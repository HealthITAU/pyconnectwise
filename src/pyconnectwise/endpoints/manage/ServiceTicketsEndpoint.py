from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsCountEndpoint import ServiceTicketsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdEndpoint import ServiceTicketsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsInfoEndpoint import ServiceTicketsInfoEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsSearchEndpoint import ServiceTicketsSearchEndpoint
from pyconnectwise.models.manage import Ticket
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTicketsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tickets", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceTicketsCountEndpoint(client, parent_endpoint=self))
        self.search = self._register_child_endpoint(ServiceTicketsSearchEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceTicketsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceTicketsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsIdEndpoint: The initialized ServiceTicketsIdEndpoint object.
        """
        child = ServiceTicketsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Ticket]:
        """
        Performs a GET request against the /service/tickets endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Ticket]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Ticket, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Ticket]:
        """
        Performs a GET request against the /service/tickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Ticket]: The parsed response data.
        """
        return self._parse_many(Ticket, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Ticket:
        """
        Performs a POST request against the /service/tickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("POST", data=data, params=params).json())
