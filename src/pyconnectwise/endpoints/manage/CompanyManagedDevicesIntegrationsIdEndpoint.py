from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdInfoEndpoint import CompanyManagedDevicesIntegrationsIdInfoEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdUsagesEndpoint import CompanyManagedDevicesIntegrationsIdUsagesEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint import CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdLoginsEndpoint import CompanyManagedDevicesIntegrationsIdLoginsEndpoint
from pyconnectwise.endpoints.manage.CompanyManagedDevicesIntegrationsIdNotificationsEndpoint import CompanyManagedDevicesIntegrationsIdNotificationsEndpoint
from pyconnectwise.models.manage.ManagedDevicesIntegrationModel import ManagedDevicesIntegrationModel

class CompanyManagedDevicesIntegrationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.crossReferences = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint(client, parent_endpoint=self)
        )
        self.logins = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdLoginsEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdNotificationsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagedDevicesIntegrationModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id} endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationModel:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationModel:
        """
        Performs a PUT request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationModel:
        """
        Performs a PATCH request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("PATCH", params=params).json())
        