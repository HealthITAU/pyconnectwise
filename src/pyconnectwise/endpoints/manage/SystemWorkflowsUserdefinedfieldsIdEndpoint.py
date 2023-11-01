from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import WorkflowActionUserDefinedField
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemWorkflowsUserdefinedfieldsIdEndpoint(
    ConnectWiseEndpoint,
    IPuttable[WorkflowActionUserDefinedField, ConnectWiseManageRequestParams],
    IPatchable[WorkflowActionUserDefinedField, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IPuttable.__init__(self, WorkflowActionUserDefinedField)
        IPatchable.__init__(self, WorkflowActionUserDefinedField)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
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
            WorkflowActionUserDefinedField,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
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
            WorkflowActionUserDefinedField,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
