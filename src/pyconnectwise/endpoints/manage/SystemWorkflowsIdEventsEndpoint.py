from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdEndpoint import SystemWorkflowsIdEventsIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsCountEndpoint import SystemWorkflowsIdEventsCountEndpoint
from pyconnectwise.models.manage.WorkflowEventModel import WorkflowEventModel

class SystemWorkflowsIdEventsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "events", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdEventsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemWorkflowsIdEventsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdEventsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdEventsIdEndpoint: The initialized SystemWorkflowsIdEventsIdEndpoint object.
        """
        child = SystemWorkflowsIdEventsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowEventModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/events endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowEventModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowEventModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowEventModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/events endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowEventModel]: The parsed response data.
        """
        return self._parse_many(WorkflowEventModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowEventModel:
        """
        Performs a POST request against the /system/workflows/{parentId}/events endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEventModel: The parsed response data.
        """
        return self._parse_one(WorkflowEventModel, super().make_request("POST", params=params).json())
        