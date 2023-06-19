from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersIdOptionsCountEndpoint import SystemWorkflowsIdTriggersIdOptionsCountEndpoint
from pyconnectwise.models.manage.WorkflowTriggerOptionModel import WorkflowTriggerOptionModel

class SystemWorkflowsIdTriggersIdOptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "options", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdTriggersIdOptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowTriggerOptionModel]:
        """
        Performs a GET request against the /system/workflows/{grandparentId}/triggers/{parentId}/options endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowTriggerOptionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowTriggerOptionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowTriggerOptionModel]:
        """
        Performs a GET request against the /system/workflows/{grandparentId}/triggers/{parentId}/options endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTriggerOptionModel]: The parsed response data.
        """
        return self._parse_many(WorkflowTriggerOptionModel, super().make_request("GET", params=params).json())
        