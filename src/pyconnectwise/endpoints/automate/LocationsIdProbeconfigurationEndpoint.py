from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechProbeConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    PatchRequestData,
)


class LocationsIdProbeconfigurationEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechProbeConfiguration, ConnectWiseAutomateRequestParams],
    IPostable[LabTechProbeConfiguration, ConnectWiseAutomateRequestParams],
    IPatchable[LabTechProbeConfiguration, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechProbeConfiguration, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Probeconfiguration", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, LabTechProbeConfiguration)
        IPostable.__init__(self, LabTechProbeConfiguration)
        IPatchable.__init__(self, LabTechProbeConfiguration)
        IPaginateable.__init__(self, LabTechProbeConfiguration)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechProbeConfiguration]:
        """
        Performs a GET request against the /Locations/{id}/Probeconfiguration endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechProbeConfiguration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechProbeConfiguration,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProbeConfiguration:
        """
        Performs a GET request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeConfiguration,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProbeConfiguration:
        """
        Performs a POST request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeConfiguration,
            super()._make_request("POST", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProbeConfiguration:
        """
        Performs a PATCH request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeConfiguration,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
