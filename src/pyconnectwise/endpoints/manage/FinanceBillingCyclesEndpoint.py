from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceBillingCyclesIdEndpoint import FinanceBillingCyclesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingCyclesCountEndpoint import FinanceBillingCyclesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingCyclesInfoEndpoint import FinanceBillingCyclesInfoEndpoint
from pyconnectwise.models.manage.BillingCycleModel import BillingCycleModel

class FinanceBillingCyclesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingCycles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingCyclesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingCyclesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceBillingCyclesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingCyclesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingCyclesIdEndpoint: The initialized FinanceBillingCyclesIdEndpoint object.
        """
        child = FinanceBillingCyclesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BillingCycleModel]:
        """
        Performs a GET request against the /finance/billingCycles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingCycleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BillingCycleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingCycleModel]:
        """
        Performs a GET request against the /finance/billingCycles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingCycleModel]: The parsed response data.
        """
        return self._parse_many(BillingCycleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingCycleModel:
        """
        Performs a POST request against the /finance/billingCycles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingCycleModel: The parsed response data.
        """
        return self._parse_one(BillingCycleModel, super().make_request("POST", params=params).json())
        