from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Models import FeatureFlag
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FeatureflagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Featureflags", parent_endpoint=parent_endpoint)

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> FeatureFlag:
        """
        Performs a POST request against the /Featureflags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            FeatureFlag: The parsed response data.
        """
        return self._parse_one(
            FeatureFlag, super()._make_request("POST", data=data, params=params).json()
        )
