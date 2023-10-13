from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import AgreementType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAgreementsTypesIdCopyEndpoint(
    ConnectWiseEndpoint, IPostable[AgreementType, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "copy", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, AgreementType)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AgreementType:
        """
        Performs a POST request against the /finance/agreements/types/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementType: The parsed response data.
        """
        return self._parse_one(AgreementType, super()._make_request("POST", data=data, params=params).json())
