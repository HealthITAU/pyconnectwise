from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPuttable,
)
from pyconnectwise.models.automate import LabTechProbeConfigurationCredentials
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ProbeconfigurationIdAgentpushcredentialsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechProbeConfigurationCredentials], ConnectWiseAutomateRequestParams],
    IPuttable[list[LabTechProbeConfigurationCredentials], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechProbeConfigurationCredentials, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Agentpushcredentials", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechProbeConfigurationCredentials])
        IPuttable.__init__(self, list[LabTechProbeConfigurationCredentials])
        IPaginateable.__init__(self, LabTechProbeConfigurationCredentials)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechProbeConfigurationCredentials]:
        """
        Performs a GET request against the /Probeconfiguration/{id}/Agentpushcredentials endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechProbeConfigurationCredentials]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechProbeConfigurationCredentials,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechProbeConfigurationCredentials]:
        """
        Performs a GET request against the /Probeconfiguration/{id}/Agentpushcredentials endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechProbeConfigurationCredentials]: The parsed response data.
        """
        return self._parse_many(
            LabTechProbeConfigurationCredentials,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechProbeConfigurationCredentials]:
        """
        Performs a PUT request against the /Probeconfiguration/{id}/Agentpushcredentials endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechProbeConfigurationCredentials]: The parsed response data.
        """
        return self._parse_many(
            LabTechProbeConfigurationCredentials,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /Probeconfiguration/{id}/Agentpushcredentials endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
