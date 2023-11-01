from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import LabTechProbeConfiguration
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ProbeconfigurationEnableprobeIdEndpoint(
    ConnectWiseEndpoint,
    IPostable[LabTechProbeConfiguration, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, LabTechProbeConfiguration)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProbeConfiguration:
        """
        Performs a POST request against the /Probeconfiguration/Enableprobe/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeConfiguration,
            super()._make_request("POST", data=data, params=params).json(),
        )
