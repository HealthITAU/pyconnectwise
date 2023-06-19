from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint import CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdLoginsCountEndpoint import CompanyManagedDevicesIntegrationsIdLoginsCountEndpoint
from pyconnectwise.models.manage.ManagedDevicesIntegrationLoginModel import ManagedDevicesIntegrationLoginModel

class CompanyManagedDevicesIntegrationsIdLoginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "logins", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdLoginsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint: The initialized CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint object.
        """
        child = CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagedDevicesIntegrationLoginModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{parentId}/logins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationLoginModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagedDevicesIntegrationLoginModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagedDevicesIntegrationLoginModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{parentId}/logins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegrationLoginModel]: The parsed response data.
        """
        return self._parse_many(ManagedDevicesIntegrationLoginModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationLoginModel:
        """
        Performs a POST request against the /company/managedDevicesIntegrations/{parentId}/logins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationLoginModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationLoginModel, super().make_request("POST", params=params).json())
        