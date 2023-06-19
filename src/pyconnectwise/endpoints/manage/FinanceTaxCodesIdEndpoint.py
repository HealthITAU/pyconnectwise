from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdCopyEndpoint import FinanceTaxCodesIdCopyEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdInfoEndpoint import FinanceTaxCodesIdInfoEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdUsagesEndpoint import FinanceTaxCodesIdUsagesEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdExpenseTypeExemptionsEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdProductTypeExemptionsEndpoint import FinanceTaxCodesIdProductTypeExemptionsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdTaxCodeLevelsEndpoint import FinanceTaxCodesIdTaxCodeLevelsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdTaxCodeXRefsEndpoint import FinanceTaxCodesIdTaxCodeXRefsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdWorkRoleExemptionsEndpoint import FinanceTaxCodesIdWorkRoleExemptionsEndpoint
from pyconnectwise.models.manage.TaxCodeModel import TaxCodeModel

class FinanceTaxCodesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            FinanceTaxCodesIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceTaxCodesIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            FinanceTaxCodesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.expenseTypeExemptions = self.register_child_endpoint(
            FinanceTaxCodesIdExpenseTypeExemptionsEndpoint(client, parent_endpoint=self)
        )
        self.productTypeExemptions = self.register_child_endpoint(
            FinanceTaxCodesIdProductTypeExemptionsEndpoint(client, parent_endpoint=self)
        )
        self.taxCodeLevels = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeLevelsEndpoint(client, parent_endpoint=self)
        )
        self.taxCodeXRefs = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeXRefsEndpoint(client, parent_endpoint=self)
        )
        self.workRoleExemptions = self.register_child_endpoint(
            FinanceTaxCodesIdWorkRoleExemptionsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxCodeModel]:
        """
        Performs a GET request against the /finance/taxCodes/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxCodeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeModel:
        """
        Performs a GET request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeModel: The parsed response data.
        """
        return self._parse_one(TaxCodeModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeModel:
        """
        Performs a PUT request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeModel: The parsed response data.
        """
        return self._parse_one(TaxCodeModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeModel:
        """
        Performs a PATCH request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeModel: The parsed response data.
        """
        return self._parse_one(TaxCodeModel, super().make_request("PATCH", params=params).json())
        