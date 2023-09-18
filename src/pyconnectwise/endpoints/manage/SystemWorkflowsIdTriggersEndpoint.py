from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersCountEndpoint import SystemWorkflowsIdTriggersCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersIdEndpoint import SystemWorkflowsIdTriggersIdEndpoint
from pyconnectwise.models.manage import WorkflowTrigger
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsIdTriggersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "triggers", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemWorkflowsIdTriggersCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemWorkflowsIdTriggersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdTriggersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdTriggersIdEndpoint: The initialized SystemWorkflowsIdTriggersIdEndpoint object.
        """
        child = SystemWorkflowsIdTriggersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[WorkflowTrigger]:
        """
        Performs a GET request against the /system/workflows/{id}/triggers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowTrigger]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowTrigger, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowTrigger]:
        """
        Performs a GET request against the /system/workflows/{id}/triggers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTrigger]: The parsed response data.
        """
        return self._parse_many(WorkflowTrigger, super()._make_request("GET", data=data, params=params).json())
