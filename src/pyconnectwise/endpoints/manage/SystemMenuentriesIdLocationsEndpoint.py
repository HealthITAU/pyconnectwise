from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesIdLocationsCountEndpoint import \
    SystemMenuentriesIdLocationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesIdLocationsIdEndpoint import SystemMenuentriesIdLocationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import MenuEntryLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMenuentriesIdLocationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MenuEntryLocation], ConnectWiseManageRequestParams],
    IPostable[MenuEntryLocation, ConnectWiseManageRequestParams],
    IPaginateable[MenuEntryLocation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "locations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[MenuEntryLocation])
        IPostable.__init__(self, MenuEntryLocation)
        IPaginateable.__init__(self, MenuEntryLocation)

        self.count = self._register_child_endpoint(
            SystemMenuentriesIdLocationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMenuentriesIdLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMenuentriesIdLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMenuentriesIdLocationsIdEndpoint: The initialized SystemMenuentriesIdLocationsIdEndpoint object.
        """
        child = SystemMenuentriesIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[MenuEntryLocation]:
        """
        Performs a GET request against the /system/menuEntries/{id}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MenuEntryLocation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), MenuEntryLocation, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[MenuEntryLocation]:
        """
        Performs a GET request against the /system/menuEntries/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MenuEntryLocation]: The parsed response data.
        """
        return self._parse_many(MenuEntryLocation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> MenuEntryLocation:
        """
        Performs a POST request against the /system/menuEntries/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MenuEntryLocation: The parsed response data.
        """
        return self._parse_one(MenuEntryLocation, super()._make_request("POST", data=data, params=params).json())
