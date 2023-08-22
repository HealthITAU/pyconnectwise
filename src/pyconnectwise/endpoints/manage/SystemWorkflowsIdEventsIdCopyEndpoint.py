from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import WorkflowEvent
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsIdEventsIdCopyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "copy", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowEvent:
        """
        Performs a POST request against the /system/workflows/{id}/events/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEvent: The parsed response data.
        """
        return self._parse_one(WorkflowEvent, super()._make_request("POST", data=data, params=params).json())
