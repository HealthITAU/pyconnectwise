from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsCountEndpoint import SystemInfoDepartmentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsIdEndpoint import SystemInfoDepartmentsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import DepartmentInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemInfoDepartmentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[DepartmentInfo], ConnectWiseManageRequestParams],
    IPaginateable[DepartmentInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "departments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[DepartmentInfo])
        IPaginateable.__init__(self, DepartmentInfo)

        self.count = self._register_child_endpoint(SystemInfoDepartmentsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoDepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoDepartmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoDepartmentsIdEndpoint: The initialized SystemInfoDepartmentsIdEndpoint object.
        """
        child = SystemInfoDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[DepartmentInfo]:
        """
        Performs a GET request against the /system/info/departments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), DepartmentInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[DepartmentInfo]:
        """
        Performs a GET request against the /system/info/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentInfo]: The parsed response data.
        """
        return self._parse_many(DepartmentInfo, super()._make_request("GET", data=data, params=params).json())
