from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectBillingRate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectBillingratesIdBillingratesIdEndpoint(
    ConnectWiseEndpoint, IPatchable[ProjectBillingRate, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> ProjectBillingRate:
        """
        Performs a PATCH request against the /project/billingRates/{id}/billingRates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBillingRate: The parsed response data.
        """
        return self._parse_one(ProjectBillingRate, super()._make_request("PATCH", data=data, params=params).json())
