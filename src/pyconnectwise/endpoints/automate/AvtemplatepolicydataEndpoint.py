from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechAVTemplatePolicyData
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class AvtemplatepolicydataEndpoint(
    ConnectWiseEndpoint, IPostable[LabTechAVTemplatePolicyData, ConnectWiseAutomateRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Avtemplatepolicydata", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, LabTechAVTemplatePolicyData)

    def post(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechAVTemplatePolicyData:
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
