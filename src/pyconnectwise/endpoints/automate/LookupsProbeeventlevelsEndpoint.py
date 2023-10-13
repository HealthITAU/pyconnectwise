from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechProbeEventLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class LookupsProbeeventlevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechProbeEventLevel], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechProbeEventLevel, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Probeeventlevels", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechProbeEventLevel])
        IPaginateable.__init__(self, LabTechProbeEventLevel)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechProbeEventLevel]:
        """
        Performs a GET request against the /Lookups/Probeeventlevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechProbeEventLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechProbeEventLevel, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechProbeEventLevel]:
        """
        Performs a GET request against the /Lookups/Probeeventlevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechProbeEventLevel]: The parsed response data.
        """
        return self._parse_many(LabTechProbeEventLevel, super()._make_request("GET", data=data, params=params).json())
