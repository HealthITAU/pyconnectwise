from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsEndpoint import SystemInfoDepartmentlocationsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsEndpoint import SystemInfoDepartmentsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLinksEndpoint import SystemInfoLinksEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocalesEndpoint import SystemInfoLocalesEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsEndpoint import SystemInfoLocationsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoMembersEndpoint import SystemInfoMembersEndpoint
from pyconnectwise.endpoints.manage.SystemInfoPersonasEndpoint import SystemInfoPersonasEndpoint
from pyconnectwise.endpoints.manage.SystemInfoStandardnotesEndpoint import SystemInfoStandardnotesEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import Info
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[Info, ConnectWiseManageRequestParams],
    IPaginateable[Info, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Info)
        IPaginateable.__init__(self, Info)

        self.locales = self._register_child_endpoint(SystemInfoLocalesEndpoint(client, parent_endpoint=self))
        self.locations = self._register_child_endpoint(SystemInfoLocationsEndpoint(client, parent_endpoint=self))
        self.links = self._register_child_endpoint(SystemInfoLinksEndpoint(client, parent_endpoint=self))
        self.personas = self._register_child_endpoint(SystemInfoPersonasEndpoint(client, parent_endpoint=self))
        self.standard_notes = self._register_child_endpoint(
            SystemInfoStandardnotesEndpoint(client, parent_endpoint=self)
        )
        self.departmentlocations = self._register_child_endpoint(
            SystemInfoDepartmentlocationsEndpoint(client, parent_endpoint=self)
        )
        self.departments = self._register_child_endpoint(SystemInfoDepartmentsEndpoint(client, parent_endpoint=self))
        self.members = self._register_child_endpoint(SystemInfoMembersEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Info]:
        """
        Performs a GET request against the /system/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Info]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Info, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Info:
        """
        Performs a GET request against the /system/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Info: The parsed response data.
        """
        return self._parse_one(Info, super()._make_request("GET", data=data, params=params).json())
