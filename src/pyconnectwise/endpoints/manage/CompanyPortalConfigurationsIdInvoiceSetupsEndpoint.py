from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdInvoiceSetupsCountEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsCountEndpoint
from pyconnectwise.models.manage.PortalConfigurationInvoiceSetupModel import PortalConfigurationInvoiceSetupModel

class CompanyPortalConfigurationsIdInvoiceSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsIdInvoiceSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint: The initialized CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint object.
        """
        child = CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationInvoiceSetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/invoiceSetups endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfigurationInvoiceSetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/invoiceSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationInvoiceSetupModel]: The parsed response data.
        """
        return self._parse_many(PortalConfigurationInvoiceSetupModel, super().make_request("GET", params=params).json())
        