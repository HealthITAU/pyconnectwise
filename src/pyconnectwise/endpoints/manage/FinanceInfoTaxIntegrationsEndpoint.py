from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceInfoTaxIntegrationsIdEndpoint import FinanceInfoTaxIntegrationsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoTaxIntegrationsCountEndpoint import FinanceInfoTaxIntegrationsCountEndpoint
from pyconnectwise.models.manage.TaxIntegrationInfoModel import TaxIntegrationInfoModel

class FinanceInfoTaxIntegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxIntegrations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInfoTaxIntegrationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceInfoTaxIntegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInfoTaxIntegrationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInfoTaxIntegrationsIdEndpoint: The initialized FinanceInfoTaxIntegrationsIdEndpoint object.
        """
        child = FinanceInfoTaxIntegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxIntegrationInfoModel]:
        """
        Performs a GET request against the /finance/info/taxIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxIntegrationInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxIntegrationInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxIntegrationInfoModel]:
        """
        Performs a GET request against the /finance/info/taxIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxIntegrationInfoModel]: The parsed response data.
        """
        return self._parse_many(TaxIntegrationInfoModel, super().make_request("GET", params=params).json())
        