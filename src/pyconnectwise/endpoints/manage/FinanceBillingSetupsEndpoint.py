from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceBillingSetupsIdEndpoint import FinanceBillingSetupsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingSetupsCountEndpoint import FinanceBillingSetupsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingSetupsInfoEndpoint import FinanceBillingSetupsInfoEndpoint
from pyconnectwise.models.manage.BillingSetupModel import BillingSetupModel

class FinanceBillingSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingSetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingSetupsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceBillingSetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingSetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingSetupsIdEndpoint: The initialized FinanceBillingSetupsIdEndpoint object.
        """
        child = FinanceBillingSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BillingSetupModel]:
        """
        Performs a GET request against the /finance/billingSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BillingSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingSetupModel]:
        """
        Performs a GET request against the /finance/billingSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingSetupModel]: The parsed response data.
        """
        return self._parse_many(BillingSetupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingSetupModel:
        """
        Performs a POST request against the /finance/billingSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingSetupModel: The parsed response data.
        """
        return self._parse_one(BillingSetupModel, super().make_request("POST", params=params).json())
        