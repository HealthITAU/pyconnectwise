from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksIdEndpoint import ServiceTicketsIdTasksIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksCountEndpoint import ServiceTicketsIdTasksCountEndpoint
from pyconnectwise.models.manage.TaskModel import TaskModel

class ServiceTicketsIdTasksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tasks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdTasksCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceTicketsIdTasksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsIdTasksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsIdTasksIdEndpoint: The initialized ServiceTicketsIdTasksIdEndpoint object.
        """
        child = ServiceTicketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaskModel]:
        """
        Performs a GET request against the /service/tickets/{parentId}/tasks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaskModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaskModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaskModel]:
        """
        Performs a GET request against the /service/tickets/{parentId}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaskModel]: The parsed response data.
        """
        return self._parse_many(TaskModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaskModel:
        """
        Performs a POST request against the /service/tickets/{parentId}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaskModel: The parsed response data.
        """
        return self._parse_one(TaskModel, super().make_request("POST", params=params).json())
        