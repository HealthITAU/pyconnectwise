from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEndpoint import SystemWorkflowsIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsCountEndpoint import SystemWorkflowsCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsTableTypesEndpoint import SystemWorkflowsTableTypesEndpoint
from pyconnectwise.models.manage.WorkflowModel import WorkflowModel

class SystemWorkflowsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workflows", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsCountEndpoint(client, parent_endpoint=self)
        )
        self.tableTypes = self.register_child_endpoint(
            SystemWorkflowsTableTypesEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemWorkflowsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdEndpoint: The initialized SystemWorkflowsIdEndpoint object.
        """
        child = SystemWorkflowsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowModel]:
        """
        Performs a GET request against the /system/workflows endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowModel]:
        """
        Performs a GET request against the /system/workflows endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowModel]: The parsed response data.
        """
        return self._parse_many(WorkflowModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowModel:
        """
        Performs a POST request against the /system/workflows endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowModel: The parsed response data.
        """
        return self._parse_one(WorkflowModel, super().make_request("POST", params=params).json())
        