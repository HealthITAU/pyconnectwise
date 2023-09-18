from typing import Any

from pyconnectwise.endpoints.automate.DataviewfoldersIdEndpoint import DataviewfoldersIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechDataViewFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse


class DataviewfoldersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Dataviewfolders", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> DataviewfoldersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized DataviewfoldersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            DataviewfoldersIdEndpoint: The initialized DataviewfoldersIdEndpoint object.
        """
        child = DataviewfoldersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechDataViewFolder]:
        """
        Performs a GET request against the /Dataviewfolders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechDataViewFolder]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechDataViewFolder, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechDataViewFolder]:
        """
        Performs a GET request against the /Dataviewfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechDataViewFolder]: The parsed response data.
        """
        return self._parse_many(LabTechDataViewFolder, super()._make_request("GET", data=data, params=params).json())
