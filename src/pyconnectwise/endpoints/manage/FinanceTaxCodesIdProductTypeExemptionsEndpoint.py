from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdProductTypeExemptionsIdEndpoint import FinanceTaxCodesIdProductTypeExemptionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdProductTypeExemptionsCountEndpoint import FinanceTaxCodesIdProductTypeExemptionsCountEndpoint
from pyconnectwise.models.manage.ProductTypeExemptionModel import ProductTypeExemptionModel

class FinanceTaxCodesIdProductTypeExemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "productTypeExemptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdProductTypeExemptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdProductTypeExemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdProductTypeExemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdProductTypeExemptionsIdEndpoint: The initialized FinanceTaxCodesIdProductTypeExemptionsIdEndpoint object.
        """
        child = FinanceTaxCodesIdProductTypeExemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductTypeExemptionModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/productTypeExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductTypeExemptionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProductTypeExemptionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductTypeExemptionModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/productTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductTypeExemptionModel]: The parsed response data.
        """
        return self._parse_many(ProductTypeExemptionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductTypeExemptionModel:
        """
        Performs a POST request against the /finance/taxCodes/{parentId}/productTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductTypeExemptionModel: The parsed response data.
        """
        return self._parse_one(ProductTypeExemptionModel, super().make_request("POST", params=params).json())
        