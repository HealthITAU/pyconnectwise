from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectTicketsIdEndpoint import ProjectTicketsIdEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsCountEndpoint import ProjectTicketsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsSearchEndpoint import ProjectTicketsSearchEndpoint
from pyconnectwise.models.manage.ProjectTicketModel import ProjectTicketModel

class ProjectTicketsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tickets", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsCountEndpoint(client, parent_endpoint=self)
        )
        self.search = self.register_child_endpoint(
            ProjectTicketsSearchEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectTicketsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectTicketsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectTicketsIdEndpoint: The initialized ProjectTicketsIdEndpoint object.
        """
        child = ProjectTicketsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectTicketModel]:
        """
        Performs a GET request against the /project/tickets endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTicketModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectTicketModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectTicketModel]:
        """
        Performs a GET request against the /project/tickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTicketModel]: The parsed response data.
        """
        return self._parse_many(ProjectTicketModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTicketModel:
        """
        Performs a POST request against the /project/tickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicketModel: The parsed response data.
        """
        return self._parse_one(ProjectTicketModel, super().make_request("POST", params=params).json())
        