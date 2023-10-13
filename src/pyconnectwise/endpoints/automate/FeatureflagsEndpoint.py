from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechFeatureFlag
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FeatureflagsEndpoint(ConnectWiseEndpoint, IPostable[LabTechFeatureFlag, ConnectWiseAutomateRequestParams]):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Featureflags", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, LabTechFeatureFlag)

    def post(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechFeatureFlag:
        """
        Performs a POST request against the /Featureflags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechFeatureFlag: The parsed response data.
        """
        return self._parse_one(LabTechFeatureFlag, super()._make_request("POST", data=data, params=params).json())
