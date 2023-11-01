from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
)
from pyconnectwise.models.automate import LabTechProbeSnmpConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    PatchRequestData,
)


class ProbeconfigurationIdSnmpconfigurationEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechProbeSnmpConfiguration, ConnectWiseAutomateRequestParams],
    IPatchable[LabTechProbeSnmpConfiguration, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechProbeSnmpConfiguration, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Snmpconfiguration", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, LabTechProbeSnmpConfiguration)
        IPatchable.__init__(self, LabTechProbeSnmpConfiguration)
        IPaginateable.__init__(self, LabTechProbeSnmpConfiguration)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechProbeSnmpConfiguration]:
        """
        Performs a GET request against the /Probeconfiguration/{id}/Snmpconfiguration endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechProbeSnmpConfiguration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechProbeSnmpConfiguration,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProbeSnmpConfiguration:
        """
        Performs a GET request against the /Probeconfiguration/{id}/Snmpconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeSnmpConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeSnmpConfiguration,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProbeSnmpConfiguration:
        """
        Performs a PATCH request against the /Probeconfiguration/{id}/Snmpconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeSnmpConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeSnmpConfiguration,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
