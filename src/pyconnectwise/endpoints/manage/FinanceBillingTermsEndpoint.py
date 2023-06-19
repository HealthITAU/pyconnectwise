from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceBillingTermsIdEndpoint import FinanceBillingTermsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingTermsCountEndpoint import FinanceBillingTermsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingTermsInfoEndpoint import FinanceBillingTermsInfoEndpoint
from pyconnectwise.models.manage.BillingTermModel import BillingTermModel

class FinanceBillingTermsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingTerms", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingTermsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingTermsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceBillingTermsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingTermsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingTermsIdEndpoint: The initialized FinanceBillingTermsIdEndpoint object.
        """
        child = FinanceBillingTermsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BillingTermModel]:
        """
        Performs a GET request against the /finance/billingTerms endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingTermModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BillingTermModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingTermModel]:
        """
        Performs a GET request against the /finance/billingTerms endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingTermModel]: The parsed response data.
        """
        return self._parse_many(BillingTermModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingTermModel:
        """
        Performs a POST request against the /finance/billingTerms endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingTermModel: The parsed response data.
        """
        return self._parse_one(BillingTermModel, super().make_request("POST", params=params).json())
        