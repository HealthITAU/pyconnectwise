from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechAVTemplatePolicyData
from pyconnectwise.responses.paginated_response import PaginatedResponse


class AvtemplatepolicydataEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Avtemplatepolicydata", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechAVTemplatePolicyData:
        """
        Performs a POST request against the /Avtemplatepolicydata endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechAVTemplatePolicyData: The parsed response data.
        """
        return self._parse_one(
            LabTechAVTemplatePolicyData, super()._make_request("POST", data=data, params=params).json()
        )
