from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsEndpoint import SystemInfoDepartmentlocationsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsEndpoint import SystemInfoDepartmentsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLinksEndpoint import SystemInfoLinksEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocalesEndpoint import SystemInfoLocalesEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsEndpoint import SystemInfoLocationsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoMembersEndpoint import SystemInfoMembersEndpoint
from pyconnectwise.endpoints.manage.SystemInfoPersonasEndpoint import SystemInfoPersonasEndpoint
from pyconnectwise.endpoints.manage.SystemInfoStandardNotesEndpoint import SystemInfoStandardNotesEndpoint
from pyconnectwise.models.manage.InfoModel import InfoModel

class SystemInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.departmentlocations = self.register_child_endpoint(
            SystemInfoDepartmentlocationsEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            SystemInfoDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.links = self.register_child_endpoint(
            SystemInfoLinksEndpoint(client, parent_endpoint=self)
        )
        self.locales = self.register_child_endpoint(
            SystemInfoLocalesEndpoint(client, parent_endpoint=self)
        )
        self.locations = self.register_child_endpoint(
            SystemInfoLocationsEndpoint(client, parent_endpoint=self)
        )
        self.members = self.register_child_endpoint(
            SystemInfoMembersEndpoint(client, parent_endpoint=self)
        )
        self.personas = self.register_child_endpoint(
            SystemInfoPersonasEndpoint(client, parent_endpoint=self)
        )
        self.standardNotes = self.register_child_endpoint(
            SystemInfoStandardNotesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InfoModel]:
        """
        Performs a GET request against the /system/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InfoModel:
        """
        Performs a GET request against the /system/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InfoModel: The parsed response data.
        """
        return self._parse_one(InfoModel, super().make_request("GET", params=params).json())
        