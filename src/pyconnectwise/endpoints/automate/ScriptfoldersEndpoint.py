from typing import Any

from pyconnectwise.endpoints.automate.ScriptfoldersHierarchyEndpoint import (
    ScriptfoldersHierarchyEndpoint,
)
from pyconnectwise.endpoints.automate.ScriptfoldersIdEndpoint import (
    ScriptfoldersIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Models import ScriptFolder
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptfoldersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Scriptfolders", parent_endpoint=parent_endpoint)

        self.hierarchy = self._register_child_endpoint(
            ScriptfoldersHierarchyEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScriptfoldersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScriptfoldersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScriptfoldersIdEndpoint: The initialized ScriptfoldersIdEndpoint object.
        """
        child = ScriptfoldersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScriptFolder]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScriptFolder,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[ScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScriptFolder]: The parsed response data.
        """
        return self._parse_many(
            ScriptFolder, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> ScriptFolder:
        """
        Performs a POST request against the /Scriptfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScriptFolder: The parsed response data.
        """
        return self._parse_one(
            ScriptFolder, super()._make_request("POST", data=data, params=params).json()
        )
