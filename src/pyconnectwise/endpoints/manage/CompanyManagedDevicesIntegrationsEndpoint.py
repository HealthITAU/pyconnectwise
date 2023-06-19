from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdEndpoint import CompanyManagedDevicesIntegrationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsCountEndpoint import CompanyManagedDevicesIntegrationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsInfoEndpoint import CompanyManagedDevicesIntegrationsInfoEndpoint
from pyconnectwise.models.manage.ManagedDevicesIntegrationModel import ManagedDevicesIntegrationModel

class CompanyManagedDevicesIntegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managedDevicesIntegrations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyManagedDevicesIntegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagedDevicesIntegrationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagedDevicesIntegrationsIdEndpoint: The initialized CompanyManagedDevicesIntegrationsIdEndpoint object.
        """
        child = CompanyManagedDevicesIntegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagedDevicesIntegrationModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagedDevicesIntegrationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagedDevicesIntegrationModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegrationModel]: The parsed response data.
        """
        return self._parse_many(ManagedDevicesIntegrationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationModel:
        """
        Performs a POST request against the /company/managedDevicesIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("POST", params=params).json())
        