from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class PatchactionsSettoteststageEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Settoteststage", parent_endpoint=parent_endpoint
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> None:
        """
        Performs a POST request against the /Patchactions/Settoteststage endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("POST", data=data, params=params)
