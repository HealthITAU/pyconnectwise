from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksCountEndpoint import ServiceTicketlinksCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksIdEndpoint import ServiceTicketlinksIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksInfoEndpoint import ServiceTicketlinksInfoEndpoint
from pyconnectwise.models.manage import ServiceTicketLink
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTicketlinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ticketLinks", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceTicketlinksCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceTicketlinksInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceTicketlinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketlinksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketlinksIdEndpoint: The initialized ServiceTicketlinksIdEndpoint object.
        """
        child = ServiceTicketlinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ServiceTicketLink]:
        """
        Performs a GET request against the /service/ticketLinks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTicketLink]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceTicketLink, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceTicketLink]:
        """
        Performs a GET request against the /service/ticketLinks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceTicketLink]: The parsed response data.
        """
        return self._parse_many(ServiceTicketLink, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceTicketLink:
        """
        Performs a POST request against the /service/ticketLinks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceTicketLink: The parsed response data.
        """
        return self._parse_one(ServiceTicketLink, super()._make_request("POST", data=data, params=params).json())
