from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsIdDepartmentsCountEndpoint import \
    SystemLocationsIdDepartmentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsIdDepartmentsIdEndpoint import SystemLocationsIdDepartmentsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import LocationDepartment
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemLocationsIdDepartmentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LocationDepartment], ConnectWiseManageRequestParams],
    IPaginateable[LocationDepartment, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "departments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LocationDepartment])
        IPaginateable.__init__(self, LocationDepartment)

        self.count = self._register_child_endpoint(
            SystemLocationsIdDepartmentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemLocationsIdDepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLocationsIdDepartmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLocationsIdDepartmentsIdEndpoint: The initialized SystemLocationsIdDepartmentsIdEndpoint object.
        """
        child = SystemLocationsIdDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[LocationDepartment]:
        """
        Performs a GET request against the /system/locations/{id}/departments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationDepartment]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LocationDepartment, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[LocationDepartment]:
        """
        Performs a GET request against the /system/locations/{id}/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocationDepartment]: The parsed response data.
        """
        return self._parse_many(LocationDepartment, super()._make_request("GET", data=data, params=params).json())
