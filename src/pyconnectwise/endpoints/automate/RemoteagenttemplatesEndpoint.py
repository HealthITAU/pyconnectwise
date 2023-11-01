from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechRemoteAgentTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class RemoteagenttemplatesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechRemoteAgentTemplate], ConnectWiseAutomateRequestParams],
    IPostable[LabTechRemoteAgentTemplate, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechRemoteAgentTemplate, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Remoteagenttemplates", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechRemoteAgentTemplate])
        IPostable.__init__(self, LabTechRemoteAgentTemplate)
        IPaginateable.__init__(self, LabTechRemoteAgentTemplate)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechRemoteAgentTemplate]:
        """
        Performs a GET request against the /Remoteagenttemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechRemoteAgentTemplate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechRemoteAgentTemplate,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechRemoteAgentTemplate]:
        """
        Performs a GET request against the /Remoteagenttemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechRemoteAgentTemplate]: The parsed response data.
        """
        return self._parse_many(
            LabTechRemoteAgentTemplate,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechRemoteAgentTemplate:
        """
        Performs a POST request against the /Remoteagenttemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechRemoteAgentTemplate: The parsed response data.
        """
        return self._parse_one(
            LabTechRemoteAgentTemplate,
            super()._make_request("POST", data=data, params=params).json(),
        )
