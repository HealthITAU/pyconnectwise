from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceCurrenciesIdInfoEndpoint import FinanceCurrenciesIdInfoEndpoint
from pyconnectwise.endpoints.manage.FinanceCurrenciesIdUsagesEndpoint import FinanceCurrenciesIdUsagesEndpoint
from pyconnectwise.models.manage.CurrencyModel import CurrencyModel

class FinanceCurrenciesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            FinanceCurrenciesIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            FinanceCurrenciesIdUsagesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CurrencyModel]:
        """
        Performs a GET request against the /finance/currencies/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CurrencyModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CurrencyModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CurrencyModel:
        """
        Performs a GET request against the /finance/currencies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CurrencyModel: The parsed response data.
        """
        return self._parse_one(CurrencyModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CurrencyModel:
        """
        Performs a PUT request against the /finance/currencies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CurrencyModel: The parsed response data.
        """
        return self._parse_one(CurrencyModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CurrencyModel:
        """
        Performs a PATCH request against the /finance/currencies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CurrencyModel: The parsed response data.
        """
        return self._parse_one(CurrencyModel, super().make_request("PATCH", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /finance/currencies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        