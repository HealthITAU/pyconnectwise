from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceTicketLinksIdEndpoint import ServiceTicketLinksIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketLinksCountEndpoint import ServiceTicketLinksCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketLinksInfoEndpoint import ServiceTicketLinksInfoEndpoint
from pyconnectwise.models.manage.ServiceTicketLinkModel import ServiceTicketLinkModel

class ServiceTicketLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ticketLinks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketLinksCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTicketLinksInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceTicketLinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketLinksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketLinksIdEndpoint: The initialized ServiceTicketLinksIdEndpoint object.
        """
        child = ServiceTicketLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceTicketLinkModel]:
        """
        Performs a GET request against the /service/ticketLinks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTicketLinkModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceTicketLinkModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceTicketLinkModel]:
        """
        Performs a GET request against the /service/ticketLinks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceTicketLinkModel]: The parsed response data.
        """
        return self._parse_many(ServiceTicketLinkModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceTicketLinkModel:
        """
        Performs a POST request against the /service/ticketLinks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceTicketLinkModel: The parsed response data.
        """
        return self._parse_one(ServiceTicketLinkModel, super().make_request("POST", params=params).json())
        