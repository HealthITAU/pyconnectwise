from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifyTypesIdEndpoint import SystemWorkflowsIdNotifyTypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifyTypesCountEndpoint import SystemWorkflowsIdNotifyTypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifyTypesInfoEndpoint import SystemWorkflowsIdNotifyTypesInfoEndpoint
from pyconnectwise.models.manage.WorkflowNotifyTypeModel import WorkflowNotifyTypeModel

class SystemWorkflowsIdNotifyTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifyTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdNotifyTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemWorkflowsIdNotifyTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemWorkflowsIdNotifyTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdNotifyTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdNotifyTypesIdEndpoint: The initialized SystemWorkflowsIdNotifyTypesIdEndpoint object.
        """
        child = SystemWorkflowsIdNotifyTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowNotifyTypeModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/notifyTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowNotifyTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowNotifyTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowNotifyTypeModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/notifyTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowNotifyTypeModel]: The parsed response data.
        """
        return self._parse_many(WorkflowNotifyTypeModel, super().make_request("GET", params=params).json())
        