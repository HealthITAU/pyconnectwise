from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsEndpoint import SystemDepartmentsIdLocationsEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdUsagesEndpoint import SystemDepartmentsIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Department
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemDepartmentsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Department, ConnectWiseManageRequestParams],
    IPuttable[Department, ConnectWiseManageRequestParams],
    IPatchable[Department, ConnectWiseManageRequestParams],
    IPaginateable[Department, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Department)
        IPuttable.__init__(self, Department)
        IPatchable.__init__(self, Department)
        IPaginateable.__init__(self, Department)

        self.usages = self._register_child_endpoint(SystemDepartmentsIdUsagesEndpoint(client, parent_endpoint=self))
        self.locations = self._register_child_endpoint(
            SystemDepartmentsIdLocationsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Department]:
        """
        Performs a GET request against the /system/departments/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Department]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Department, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Department:
        """
        Performs a GET request against the /system/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Department: The parsed response data.
        """
        return self._parse_one(Department, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /system/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Department:
        """
        Performs a PUT request against the /system/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Department: The parsed response data.
        """
        return self._parse_one(Department, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Department:
        """
        Performs a PATCH request against the /system/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Department: The parsed response data.
        """
        return self._parse_one(Department, super()._make_request("PATCH", data=data, params=params).json())
