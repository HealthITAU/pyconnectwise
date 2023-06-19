from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdTaxCodeXRefsIdEndpoint import FinanceTaxCodesIdTaxCodeXRefsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdTaxCodeXRefsCountEndpoint import FinanceTaxCodesIdTaxCodeXRefsCountEndpoint
from pyconnectwise.models.manage.TaxCodeXRefModel import TaxCodeXRefModel

class FinanceTaxCodesIdTaxCodeXRefsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodeXRefs", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeXRefsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdTaxCodeXRefsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdTaxCodeXRefsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdTaxCodeXRefsIdEndpoint: The initialized FinanceTaxCodesIdTaxCodeXRefsIdEndpoint object.
        """
        child = FinanceTaxCodesIdTaxCodeXRefsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxCodeXRefModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/taxCodeXRefs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeXRefModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxCodeXRefModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxCodeXRefModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/taxCodeXRefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCodeXRefModel]: The parsed response data.
        """
        return self._parse_many(TaxCodeXRefModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeXRefModel:
        """
        Performs a POST request against the /finance/taxCodes/{parentId}/taxCodeXRefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeXRefModel: The parsed response data.
        """
        return self._parse_one(TaxCodeXRefModel, super().make_request("POST", params=params).json())
        