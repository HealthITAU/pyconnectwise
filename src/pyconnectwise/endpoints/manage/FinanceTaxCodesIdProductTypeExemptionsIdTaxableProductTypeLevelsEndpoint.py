from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint import FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsCountEndpoint import FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsCountEndpoint
from pyconnectwise.models.manage.TaxableProductTypeLevelModel import TaxableProductTypeLevelModel

class FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableProductTypeLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint: The initialized FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint object.
        """
        child = FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxableProductTypeLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableProductTypeLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxableProductTypeLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableProductTypeLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableProductTypeLevelModel]: The parsed response data.
        """
        return self._parse_many(TaxableProductTypeLevelModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableProductTypeLevelModel:
        """
        Performs a POST request against the /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableProductTypeLevelModel: The parsed response data.
        """
        return self._parse_one(TaxableProductTypeLevelModel, super().make_request("POST", params=params).json())
        