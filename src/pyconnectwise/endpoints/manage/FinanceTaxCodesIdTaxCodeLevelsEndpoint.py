from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdTaxCodeLevelsIdEndpoint import FinanceTaxCodesIdTaxCodeLevelsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdTaxCodeLevelsCountEndpoint import FinanceTaxCodesIdTaxCodeLevelsCountEndpoint
from pyconnectwise.models.manage.TaxCodeLevelModel import TaxCodeLevelModel

class FinanceTaxCodesIdTaxCodeLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodeLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdTaxCodeLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdTaxCodeLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdTaxCodeLevelsIdEndpoint: The initialized FinanceTaxCodesIdTaxCodeLevelsIdEndpoint object.
        """
        child = FinanceTaxCodesIdTaxCodeLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxCodeLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/taxCodeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxCodeLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxCodeLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/taxCodeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCodeLevelModel]: The parsed response data.
        """
        return self._parse_many(TaxCodeLevelModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeLevelModel:
        """
        Performs a POST request against the /finance/taxCodes/{parentId}/taxCodeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeLevelModel: The parsed response data.
        """
        return self._parse_one(TaxCodeLevelModel, super().make_request("POST", params=params).json())
        