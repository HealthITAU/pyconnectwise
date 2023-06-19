from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdEndpoint import CompanyPortalConfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsCopyEndpoint import CompanyPortalConfigurationsCopyEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsCountEndpoint import CompanyPortalConfigurationsCountEndpoint
from pyconnectwise.models.manage.PortalConfigurationModel import PortalConfigurationModel

class CompanyPortalConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalConfigurations", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            CompanyPortalConfigurationsCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalConfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalConfigurationsIdEndpoint: The initialized CompanyPortalConfigurationsIdEndpoint object.
        """
        child = CompanyPortalConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationModel]:
        """
        Performs a GET request against the /company/portalConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfigurationModel]:
        """
        Performs a GET request against the /company/portalConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationModel]: The parsed response data.
        """
        return self._parse_many(PortalConfigurationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationModel:
        """
        Performs a POST request against the /company/portalConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationModel, super().make_request("POST", params=params).json())
        