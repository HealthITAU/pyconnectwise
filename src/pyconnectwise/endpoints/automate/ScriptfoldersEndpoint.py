from pyconnectwise.endpoints.automate.ScriptfoldersHierarchyEndpoint import (
    ScriptfoldersHierarchyEndpoint,
)
from pyconnectwise.endpoints.automate.ScriptfoldersIdEndpoint import (
    ScriptfoldersIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechScriptFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ScriptfoldersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechScriptFolder], ConnectWiseAutomateRequestParams],
    IPostable[LabTechScriptFolder, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechScriptFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Scriptfolders", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechScriptFolder])
        IPostable.__init__(self, LabTechScriptFolder)
        IPaginateable.__init__(self, LabTechScriptFolder)

        self.hierarchy = self._register_child_endpoint(
            ScriptfoldersHierarchyEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScriptfoldersIdEndpoint:  # noqa: A002
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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechScriptFolder]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechScriptFolder,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechScriptFolder]: The parsed response data.
        """
        return self._parse_many(
            LabTechScriptFolder,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechScriptFolder:
        """
        Performs a POST request against the /Scriptfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechScriptFolder: The parsed response data.
        """
        return self._parse_one(
            LabTechScriptFolder,
            super()._make_request("POST", data=data, params=params).json(),
        )
