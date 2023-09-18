from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechCommandExecute
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdCommandexecuteEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Commandexecute", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechCommandExecute]:
        """
        Performs a GET request against the /Computers/{id}/Commandexecute endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechCommandExecute]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechCommandExecute, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechCommandExecute]:
        """
        Performs a GET request against the /Computers/{id}/Commandexecute endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechCommandExecute]: The parsed response data.
        """
        return self._parse_many(LabTechCommandExecute, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechCommandExecute:
        """
        Performs a POST request against the /Computers/{id}/Commandexecute endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechCommandExecute: The parsed response data.
        """
        return self._parse_one(LabTechCommandExecute, super()._make_request("POST", data=data, params=params).json())
