from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsCountEndpoint import SystemInfoLocationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsIdEndpoint import SystemInfoLocationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import LocationInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemInfoLocationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LocationInfo], ConnectWiseManageRequestParams],
    IPaginateable[LocationInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "locations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LocationInfo])
        IPaginateable.__init__(self, LocationInfo)

        self.count = self._register_child_endpoint(SystemInfoLocationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoLocationsIdEndpoint: The initialized SystemInfoLocationsIdEndpoint object.
        """
        child = SystemInfoLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[LocationInfo]:
        """
        Performs a GET request against the /system/info/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LocationInfo, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[LocationInfo]:
        """
        Performs a GET request against the /system/info/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocationInfo]: The parsed response data.
        """
        return self._parse_many(LocationInfo, super()._make_request("GET", data=data, params=params).json())
