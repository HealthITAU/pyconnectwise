from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectTicketsIdTasksIdEndpoint import ProjectTicketsIdTasksIdEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdTasksCountEndpoint import ProjectTicketsIdTasksCountEndpoint
from pyconnectwise.models.manage.TicketTaskModel import TicketTaskModel

class ProjectTicketsIdTasksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tasks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsIdTasksCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectTicketsIdTasksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectTicketsIdTasksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectTicketsIdTasksIdEndpoint: The initialized ProjectTicketsIdTasksIdEndpoint object.
        """
        child = ProjectTicketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TicketTaskModel]:
        """
        Performs a GET request against the /project/tickets/{parentId}/tasks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TicketTaskModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TicketTaskModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TicketTaskModel]:
        """
        Performs a GET request against the /project/tickets/{parentId}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TicketTaskModel]: The parsed response data.
        """
        return self._parse_many(TicketTaskModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TicketTaskModel:
        """
        Performs a POST request against the /project/tickets/{parentId}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketTaskModel: The parsed response data.
        """
        return self._parse_one(TicketTaskModel, super().make_request("POST", params=params).json())
        