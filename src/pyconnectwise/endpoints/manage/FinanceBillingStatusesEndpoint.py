from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceBillingStatusesIdEndpoint import FinanceBillingStatusesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingStatusesCountEndpoint import FinanceBillingStatusesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingStatusesInfoEndpoint import FinanceBillingStatusesInfoEndpoint
from pyconnectwise.models.manage.BillingStatusModel import BillingStatusModel

class FinanceBillingStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingStatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceBillingStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingStatusesIdEndpoint: The initialized FinanceBillingStatusesIdEndpoint object.
        """
        child = FinanceBillingStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BillingStatusModel]:
        """
        Performs a GET request against the /finance/billingStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BillingStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingStatusModel]:
        """
        Performs a GET request against the /finance/billingStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingStatusModel]: The parsed response data.
        """
        return self._parse_many(BillingStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingStatusModel:
        """
        Performs a POST request against the /finance/billingStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingStatusModel: The parsed response data.
        """
        return self._parse_one(BillingStatusModel, super().make_request("POST", params=params).json())
        