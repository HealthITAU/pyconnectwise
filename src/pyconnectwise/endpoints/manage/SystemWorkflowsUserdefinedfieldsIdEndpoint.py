from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import WorkflowActionUserDefinedField
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsUserdefinedfieldsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionUserDefinedField:
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

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionUserDefinedField:
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
