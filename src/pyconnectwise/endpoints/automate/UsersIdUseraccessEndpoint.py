from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
)
from pyconnectwise.models.automate import AutomateUserAccess
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UsersIdUseraccessEndpoint(
    ConnectWiseEndpoint, IGettable[AutomateUserAccess, ConnectWiseAutomateRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Useraccess", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, AutomateUserAccess)

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateUserAccess:
        """
        Performs a GET request against the /Users/{id}/Useraccess endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUserAccess: The parsed response data.
        """
        return self._parse_one(
            AutomateUserAccess,
            super()._make_request("GET", data=data, params=params).json(),
        )
