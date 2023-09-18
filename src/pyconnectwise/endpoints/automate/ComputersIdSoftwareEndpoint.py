from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdSoftwareIdEndpoint import ComputersIdSoftwareIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechComputerSoftware
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdSoftwareEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Software", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ComputersIdSoftwareIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ComputersIdSoftwareIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ComputersIdSoftwareIdEndpoint: The initialized ComputersIdSoftwareIdEndpoint object.
        """
        child = ComputersIdSoftwareIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechComputerSoftware]:
        """
        Performs a GET request against the /Computers/{id}/Software endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerSoftware]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechComputerSoftware, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechComputerSoftware]:
        """
        Performs a GET request against the /Computers/{id}/Software endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerSoftware]: The parsed response data.
        """
        return self._parse_many(LabTechComputerSoftware, super()._make_request("GET", data=data, params=params).json())
