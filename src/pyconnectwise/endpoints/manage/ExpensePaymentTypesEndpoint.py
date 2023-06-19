from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ExpensePaymentTypesIdEndpoint import ExpensePaymentTypesIdEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymentTypesCountEndpoint import ExpensePaymentTypesCountEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymentTypesInfoEndpoint import ExpensePaymentTypesInfoEndpoint
from pyconnectwise.models.manage.PaymentTypeModel import PaymentTypeModel

class ExpensePaymentTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpensePaymentTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ExpensePaymentTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ExpensePaymentTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpensePaymentTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpensePaymentTypesIdEndpoint: The initialized ExpensePaymentTypesIdEndpoint object.
        """
        child = ExpensePaymentTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PaymentTypeModel]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PaymentTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PaymentTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PaymentTypeModel]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PaymentTypeModel]: The parsed response data.
        """
        return self._parse_many(PaymentTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PaymentTypeModel:
        """
        Performs a POST request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaymentTypeModel: The parsed response data.
        """
        return self._parse_one(PaymentTypeModel, super().make_request("POST", params=params).json())
        