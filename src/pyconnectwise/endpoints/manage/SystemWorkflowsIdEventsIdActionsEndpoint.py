from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdActionsIdEndpoint import SystemWorkflowsIdEventsIdActionsIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdActionsCountEndpoint import SystemWorkflowsIdEventsIdActionsCountEndpoint
from pyconnectwise.models.manage.WorkflowActionModel import WorkflowActionModel

class SystemWorkflowsIdEventsIdActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "actions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdEventsIdActionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemWorkflowsIdEventsIdActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdEventsIdActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdEventsIdActionsIdEndpoint: The initialized SystemWorkflowsIdEventsIdActionsIdEndpoint object.
        """
        child = SystemWorkflowsIdEventsIdActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowActionModel]:
        """
        Performs a GET request against the /system/workflows/{grandparentId}/events/{parentId}/actions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowActionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowActionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowActionModel]:
        """
        Performs a GET request against the /system/workflows/{grandparentId}/events/{parentId}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowActionModel]: The parsed response data.
        """
        return self._parse_many(WorkflowActionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionModel:
        """
        Performs a POST request against the /system/workflows/{grandparentId}/events/{parentId}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionModel: The parsed response data.
        """
        return self._parse_one(WorkflowActionModel, super().make_request("POST", params=params).json())
        