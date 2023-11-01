from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.automate import LabTechHashMethod
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class LookupsSnmphashmethodsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechHashMethod], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechHashMethod, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Snmphashmethods", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechHashMethod])
        IPaginateable.__init__(self, LabTechHashMethod)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechHashMethod]:
        """
        Performs a GET request against the /Lookups/Snmphashmethods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechHashMethod]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechHashMethod,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechHashMethod]:
        """
        Performs a GET request against the /Lookups/Snmphashmethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechHashMethod]: The parsed response data.
        """
        return self._parse_many(
            LabTechHashMethod,
            super()._make_request("GET", data=data, params=params).json(),
        )
