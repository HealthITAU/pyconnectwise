from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsIdDepartmentsEndpoint import (
    SystemLocationsIdDepartmentsEndpoint,
)
from pyconnectwise.endpoints.manage.SystemLocationsIdUsagesEndpoint import (
    SystemLocationsIdUsagesEndpoint,
)
from pyconnectwise.endpoints.manage.SystemLocationsIdWorkrolesEndpoint import (
    SystemLocationsIdWorkrolesEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Location
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemLocationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Location, ConnectWiseManageRequestParams],
    IPuttable[Location, ConnectWiseManageRequestParams],
    IPatchable[Location, ConnectWiseManageRequestParams],
    IPaginateable[Location, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Location)
        IPuttable.__init__(self, Location)
        IPatchable.__init__(self, Location)
        IPaginateable.__init__(self, Location)

        self.usages = self._register_child_endpoint(
            SystemLocationsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.work_roles = self._register_child_endpoint(
            SystemLocationsIdWorkrolesEndpoint(client, parent_endpoint=self)
        )
        self.departments = self._register_child_endpoint(
            SystemLocationsIdDepartmentsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Location]:
        """
        Performs a GET request against the /system/locations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Location]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Location,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Location:
        """
        Performs a GET request against the /system/locations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(
            Location, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /system/locations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Location:
        """
        Performs a PUT request against the /system/locations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(
            Location, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Location:
        """
        Performs a PATCH request against the /system/locations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(
            Location, super()._make_request("PATCH", data=data, params=params).json()
        )
