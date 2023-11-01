from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPatchable,
)
from pyconnectwise.models.automate import AutomateScheduledScript
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    PatchRequestData,
)


class ScriptingScriptschedulesIdEndpoint(
    ConnectWiseEndpoint,
    IPatchable[AutomateScheduledScript, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IPatchable.__init__(self, AutomateScheduledScript)

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /Scripting/Scriptschedules/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateScheduledScript:
        """
        Performs a PATCH request against the /Scripting/Scriptschedules/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateScheduledScript: The parsed response data.
        """
        return self._parse_one(
            AutomateScheduledScript,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
