from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechVirusScannerDef
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class VirusscannerdefsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechVirusScannerDef], ConnectWiseAutomateRequestParams],
    IPostable[LabTechVirusScannerDef, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechVirusScannerDef, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Virusscannerdefs", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechVirusScannerDef])
        IPostable.__init__(self, LabTechVirusScannerDef)
        IPaginateable.__init__(self, LabTechVirusScannerDef)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechVirusScannerDef]:
        """
        Performs a GET request against the /Virusscannerdefs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechVirusScannerDef]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechVirusScannerDef,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechVirusScannerDef]:
        """
        Performs a GET request against the /Virusscannerdefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechVirusScannerDef]: The parsed response data.
        """
        return self._parse_many(
            LabTechVirusScannerDef,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechVirusScannerDef:
        """
        Performs a POST request against the /Virusscannerdefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechVirusScannerDef: The parsed response data.
        """
        return self._parse_one(
            LabTechVirusScannerDef,
            super()._make_request("POST", data=data, params=params).json(),
        )
