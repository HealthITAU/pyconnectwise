from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPatchable, IPuttable
from pyconnectwise.models.manage import WorkflowActionUserDefinedField
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowsUserdefinedfieldsIdEndpoint(
    ConnectWiseEndpoint,
    IPatchable[WorkflowActionUserDefinedField, ConnectWiseManageRequestParams],
    IPuttable[WorkflowActionUserDefinedField, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IPatchable.__init__(self, WorkflowActionUserDefinedField)
        IPuttable.__init__(self, WorkflowActionUserDefinedField)

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> WorkflowActionUserDefinedField:
        """
        Performs a PATCH request against the /system/workflows/userdefinedfields/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionUserDefinedField: The parsed response data.
        """
        return self._parse_one(
            WorkflowActionUserDefinedField, super()._make_request("PATCH", data=data, params=params).json()
        )

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> WorkflowActionUserDefinedField:
        """
        Performs a PUT request against the /system/workflows/userdefinedfields/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionUserDefinedField: The parsed response data.
        """
        return self._parse_one(
            WorkflowActionUserDefinedField, super()._make_request("PUT", data=data, params=params).json()
        )
