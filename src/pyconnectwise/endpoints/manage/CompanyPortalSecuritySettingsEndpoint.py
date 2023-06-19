from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalSecuritySettingsIdEndpoint import CompanyPortalSecuritySettingsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalSecuritySettingsCountEndpoint import CompanyPortalSecuritySettingsCountEndpoint
from pyconnectwise.models.manage.PortalSecuritySettingModel import PortalSecuritySettingModel

class CompanyPortalSecuritySettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalSecuritySettings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalSecuritySettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyPortalSecuritySettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalSecuritySettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalSecuritySettingsIdEndpoint: The initialized CompanyPortalSecuritySettingsIdEndpoint object.
        """
        child = CompanyPortalSecuritySettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalSecuritySettingModel]:
        """
        Performs a GET request against the /company/portalSecuritySettings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalSecuritySettingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalSecuritySettingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalSecuritySettingModel]:
        """
        Performs a GET request against the /company/portalSecuritySettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalSecuritySettingModel]: The parsed response data.
        """
        return self._parse_many(PortalSecuritySettingModel, super().make_request("GET", params=params).json())
        