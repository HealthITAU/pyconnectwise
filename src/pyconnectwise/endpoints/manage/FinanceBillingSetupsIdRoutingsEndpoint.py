from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceBillingSetupsIdRoutingsIdEndpoint import FinanceBillingSetupsIdRoutingsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingSetupsIdRoutingsCountEndpoint import FinanceBillingSetupsIdRoutingsCountEndpoint
from pyconnectwise.models.manage.BillingSetupRoutingModel import BillingSetupRoutingModel

class FinanceBillingSetupsIdRoutingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "routings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingSetupsIdRoutingsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceBillingSetupsIdRoutingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingSetupsIdRoutingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingSetupsIdRoutingsIdEndpoint: The initialized FinanceBillingSetupsIdRoutingsIdEndpoint object.
        """
        child = FinanceBillingSetupsIdRoutingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BillingSetupRoutingModel]:
        """
        Performs a GET request against the /finance/billingSetups/{parentId}/routings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingSetupRoutingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BillingSetupRoutingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingSetupRoutingModel]:
        """
        Performs a GET request against the /finance/billingSetups/{parentId}/routings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingSetupRoutingModel]: The parsed response data.
        """
        return self._parse_many(BillingSetupRoutingModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingSetupRoutingModel:
        """
        Performs a POST request against the /finance/billingSetups/{parentId}/routings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingSetupRoutingModel: The parsed response data.
        """
        return self._parse_one(BillingSetupRoutingModel, super().make_request("POST", params=params).json())
        