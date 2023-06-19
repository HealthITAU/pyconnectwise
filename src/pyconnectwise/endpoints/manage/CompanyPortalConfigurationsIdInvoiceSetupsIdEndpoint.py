from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdInvoiceSetupsIdTestTransactionEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsIdTestTransactionEndpoint
from pyconnectwise.models.manage.PortalConfigurationInvoiceSetupModel import PortalConfigurationInvoiceSetupModel

class CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.testTransaction = self.register_child_endpoint(
            CompanyPortalConfigurationsIdInvoiceSetupsIdTestTransactionEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationInvoiceSetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/invoiceSetups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationInvoiceSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalConfigurationInvoiceSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationInvoiceSetupModel:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetupModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationInvoiceSetupModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationInvoiceSetupModel:
        """
        Performs a PUT request against the /company/portalConfigurations/{parentId}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetupModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationInvoiceSetupModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationInvoiceSetupModel:
        """
        Performs a PATCH request against the /company/portalConfigurations/{parentId}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetupModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationInvoiceSetupModel, super().make_request("PATCH", params=params).json())
        