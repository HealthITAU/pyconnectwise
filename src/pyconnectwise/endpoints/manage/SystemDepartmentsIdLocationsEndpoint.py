from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsCountEndpoint import (
    SystemDepartmentsIdLocationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsIdEndpoint import (
    SystemDepartmentsIdLocationsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import DepartmentLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemDepartmentsIdLocationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[DepartmentLocation], ConnectWiseManageRequestParams],
    IPostable[DepartmentLocation, ConnectWiseManageRequestParams],
    IPaginateable[DepartmentLocation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "locations", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[DepartmentLocation])
        IPostable.__init__(self, DepartmentLocation)
        IPaginateable.__init__(self, DepartmentLocation)

        self.count = self._register_child_endpoint(
            SystemDepartmentsIdLocationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemDepartmentsIdLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemDepartmentsIdLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemDepartmentsIdLocationsIdEndpoint: The initialized SystemDepartmentsIdLocationsIdEndpoint object.
        """
        child = SystemDepartmentsIdLocationsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[DepartmentLocation]:
        """
        Performs a GET request against the /system/departments/{id}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentLocation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            DepartmentLocation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[DepartmentLocation]:
        """
        Performs a GET request against the /system/departments/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentLocation]: The parsed response data.
        """
        return self._parse_many(
            DepartmentLocation,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> DepartmentLocation:
        """
        Performs a POST request against the /system/departments/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DepartmentLocation: The parsed response data.
        """
        return self._parse_one(
            DepartmentLocation,
            super()._make_request("POST", data=data, params=params).json(),
        )
