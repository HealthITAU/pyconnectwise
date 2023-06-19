from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceDeliveryMethodsIdEndpoint import FinanceDeliveryMethodsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceDeliveryMethodsCountEndpoint import FinanceDeliveryMethodsCountEndpoint
from pyconnectwise.models.manage.DeliveryMethodModel import DeliveryMethodModel

class FinanceDeliveryMethodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "deliveryMethods", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceDeliveryMethodsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceDeliveryMethodsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceDeliveryMethodsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceDeliveryMethodsIdEndpoint: The initialized FinanceDeliveryMethodsIdEndpoint object.
        """
        child = FinanceDeliveryMethodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[DeliveryMethodModel]:
        """
        Performs a GET request against the /finance/deliveryMethods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DeliveryMethodModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            DeliveryMethodModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DeliveryMethodModel]:
        """
        Performs a GET request against the /finance/deliveryMethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DeliveryMethodModel]: The parsed response data.
        """
        return self._parse_many(DeliveryMethodModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DeliveryMethodModel:
        """
        Performs a POST request against the /finance/deliveryMethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DeliveryMethodModel: The parsed response data.
        """
        return self._parse_one(DeliveryMethodModel, super().make_request("POST", params=params).json())
        