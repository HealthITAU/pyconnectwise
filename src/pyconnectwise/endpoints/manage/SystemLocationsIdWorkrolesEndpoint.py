from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsIdWorkrolesCountEndpoint import \
    SystemLocationsIdWorkrolesCountEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsIdWorkrolesIdEndpoint import SystemLocationsIdWorkrolesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import LocationWorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemLocationsIdWorkrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LocationWorkRole], ConnectWiseManageRequestParams],
    IPaginateable[LocationWorkRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "workRoles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LocationWorkRole])
        IPaginateable.__init__(self, LocationWorkRole)

        self.count = self._register_child_endpoint(
            SystemLocationsIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemLocationsIdWorkrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLocationsIdWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLocationsIdWorkrolesIdEndpoint: The initialized SystemLocationsIdWorkrolesIdEndpoint object.
        """
        child = SystemLocationsIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[LocationWorkRole]:
        """
        Performs a GET request against the /system/locations/{id}/workRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationWorkRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LocationWorkRole, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[LocationWorkRole]:
        """
        Performs a GET request against the /system/locations/{id}/workRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocationWorkRole]: The parsed response data.
        """
        return self._parse_many(LocationWorkRole, super()._make_request("GET", data=data, params=params).json())
