from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
)
from pyconnectwise.models.automate import LabTechUserProfile
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UserprofilesEndpoint(ConnectWiseEndpoint, IGettable[LabTechUserProfile, ConnectWiseAutomateRequestParams]):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Userprofiles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, LabTechUserProfile)

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechUserProfile:
        """
        Performs a GET request against the /Userprofiles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechUserProfile: The parsed response data.
        """
        return self._parse_one(
            LabTechUserProfile,
            super()._make_request("GET", data=data, params=params).json(),
        )
