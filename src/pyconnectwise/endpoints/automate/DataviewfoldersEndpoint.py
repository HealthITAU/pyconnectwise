from typing import Any

from pyconnectwise.endpoints.automate.DataviewfoldersIdEndpoint import DataviewfoldersIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechDataViewFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class DataviewfoldersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechDataViewFolder], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechDataViewFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Dataviewfolders", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechDataViewFolder])
        IPaginateable.__init__(self, LabTechDataViewFolder)

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
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechDataViewFolder, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechDataViewFolder]:
        """
        Performs a GET request against the /Dataviewfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechDataViewFolder]: The parsed response data.
        """
        return self._parse_many(LabTechDataViewFolder, super()._make_request("GET", data=data, params=params).json())
