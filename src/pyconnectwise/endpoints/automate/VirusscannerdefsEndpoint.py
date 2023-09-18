from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechVirusScannerDef
from pyconnectwise.responses.paginated_response import PaginatedResponse


class VirusscannerdefsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Virusscannerdefs", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechVirusScannerDef, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechVirusScannerDef]:
        """
        Performs a GET request against the /Virusscannerdefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechVirusScannerDef]: The parsed response data.
        """
        return self._parse_many(LabTechVirusScannerDef, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechVirusScannerDef:
        """
        Performs a POST request against the /Virusscannerdefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechVirusScannerDef: The parsed response data.
        """
        return self._parse_one(LabTechVirusScannerDef, super()._make_request("POST", data=data, params=params).json())
