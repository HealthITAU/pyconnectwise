from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint import \
    SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint
from pyconnectwise.models.manage import WorkflowActionUserDefinedField
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsUserdefinedfieldsEventsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.actions = self._register_child_endpoint(
            SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint(client, parent_endpoint=self)
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionUserDefinedField:
        """
        Performs a POST request against the /system/workflows/userdefinedfields/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionUserDefinedField: The parsed response data.
        """
        return self._parse_one(
            WorkflowActionUserDefinedField, super()._make_request("POST", data=data, params=params).json()
        )
