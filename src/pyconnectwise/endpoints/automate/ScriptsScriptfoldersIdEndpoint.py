from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import AutomateSubmittableScriptFolder
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ScriptsScriptfoldersIdEndpoint(
    ConnectWiseEndpoint,
    IPostable[AutomateSubmittableScriptFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, AutomateSubmittableScriptFolder)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateSubmittableScriptFolder:
        """
        Performs a POST request against the /Scripts/Scriptfolders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateSubmittableScriptFolder: The parsed response data.
        """
        return self._parse_one(
            AutomateSubmittableScriptFolder,
            super()._make_request("POST", data=data, params=params).json(),
        )
