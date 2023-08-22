from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechAVTemplatePolicy
from pyconnectwise.responses.paginated_response import PaginatedResponse


class AvtemplatepoliciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Avtemplatepolicies", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechAVTemplatePolicy:
        """
        Performs a POST request against the /Avtemplatepolicies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechAVTemplatePolicy: The parsed response data.
        """
        return self._parse_one(LabTechAVTemplatePolicy, super()._make_request("POST", data=data, params=params).json())
