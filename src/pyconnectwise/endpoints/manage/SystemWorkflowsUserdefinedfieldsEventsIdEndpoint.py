from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint import (
    SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint,
)
from pyconnectwise.interfaces import IPostable
from pyconnectwise.models.manage import WorkflowActionUserDefinedField
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowsUserdefinedfieldsEventsIdEndpoint(
    ConnectWiseEndpoint, IPostable[WorkflowActionUserDefinedField, ConnectWiseManageRequestParams]
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, WorkflowActionUserDefinedField)

        self.actions = self._register_child_endpoint(
            SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint(client, parent_endpoint=self)
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> WorkflowActionUserDefinedField:
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
