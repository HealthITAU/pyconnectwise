from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdInvoiceSetupsEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdOpportunitySetupsEndpoint import CompanyPortalConfigurationsIdOpportunitySetupsEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint import CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdProjectSetupsEndpoint import CompanyPortalConfigurationsIdProjectSetupsEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdServiceSetupsEndpoint import CompanyPortalConfigurationsIdServiceSetupsEndpoint
from pyconnectwise.models.manage.PortalConfigurationModel import PortalConfigurationModel

class CompanyPortalConfigurationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.invoiceSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdInvoiceSetupsEndpoint(client, parent_endpoint=self)
        )
        self.opportunitySetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdOpportunitySetupsEndpoint(client, parent_endpoint=self)
        )
        self.passwordEmailSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint(client, parent_endpoint=self)
        )
        self.projectSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdProjectSetupsEndpoint(client, parent_endpoint=self)
        )
        self.serviceSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdServiceSetupsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{id} endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationModel:
        """
        Performs a GET request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationModel:
        """
        Performs a PUT request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationModel:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationModel, super().make_request("PATCH", params=params).json())
        