from pyconnectwise.endpoints.automate.ScriptsScriptfoldersIdEndpoint import (
    ScriptsScriptfoldersIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import AutomateSubmittableScriptFolder
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ScriptsScriptfoldersEndpoint(
    ConnectWiseEndpoint,
    IPostable[AutomateSubmittableScriptFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Scriptfolders", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, AutomateSubmittableScriptFolder)

    def id(self, id: int) -> ScriptsScriptfoldersIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ScriptsScriptfoldersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScriptsScriptfoldersIdEndpoint: The initialized ScriptsScriptfoldersIdEndpoint object.
        """
        child = ScriptsScriptfoldersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateSubmittableScriptFolder:
        """
        Performs a POST request against the /Scripts/Scriptfolders endpoint.

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
