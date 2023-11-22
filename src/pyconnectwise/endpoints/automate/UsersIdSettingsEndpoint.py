from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import LabTechUserSetting
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UsersIdSettingsEndpoint(ConnectWiseEndpoint, IPostable[LabTechUserSetting, ConnectWiseAutomateRequestParams]):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Settings", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, LabTechUserSetting)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechUserSetting:
        """
        Performs a POST request against the /Users/{id}/Settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechUserSetting: The parsed response data.
        """
        return self._parse_one(
            LabTechUserSetting,
            super()._make_request("POST", data=data, params=params).json(),
        )
