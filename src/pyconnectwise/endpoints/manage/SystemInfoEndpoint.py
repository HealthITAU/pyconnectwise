from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsEndpoint import SystemInfoDepartmentlocationsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsEndpoint import SystemInfoDepartmentsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLinksEndpoint import SystemInfoLinksEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocalesEndpoint import SystemInfoLocalesEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsEndpoint import SystemInfoLocationsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoMembersEndpoint import SystemInfoMembersEndpoint
from pyconnectwise.endpoints.manage.SystemInfoPersonasEndpoint import SystemInfoPersonasEndpoint
from pyconnectwise.endpoints.manage.SystemInfoStandardnotesEndpoint import SystemInfoStandardnotesEndpoint
from pyconnectwise.models.manage import Info
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.departments = self._register_child_endpoint(SystemInfoDepartmentsEndpoint(client, parent_endpoint=self))
        self.departmentlocations = self._register_child_endpoint(
            SystemInfoDepartmentlocationsEndpoint(client, parent_endpoint=self)
        )
        self.locations = self._register_child_endpoint(SystemInfoLocationsEndpoint(client, parent_endpoint=self))
        self.links = self._register_child_endpoint(SystemInfoLinksEndpoint(client, parent_endpoint=self))
        self.standard_notes = self._register_child_endpoint(
            SystemInfoStandardnotesEndpoint(client, parent_endpoint=self)
        )
        self.personas = self._register_child_endpoint(SystemInfoPersonasEndpoint(client, parent_endpoint=self))
        self.locales = self._register_child_endpoint(SystemInfoLocalesEndpoint(client, parent_endpoint=self))
        self.members = self._register_child_endpoint(SystemInfoMembersEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Info]:
        """
        Performs a GET request against the /system/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Info]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Info, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Info:
        """
        Performs a GET request against the /system/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Info: The parsed response data.
        """
        return self._parse_one(Info, super()._make_request("GET", data=data, params=params).json())
