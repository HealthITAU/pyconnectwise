from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymenttypesCountEndpoint import ExpensePaymenttypesCountEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymenttypesIdEndpoint import ExpensePaymenttypesIdEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymenttypesInfoEndpoint import ExpensePaymenttypesInfoEndpoint
from pyconnectwise.models.manage import PaymentType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ExpensePaymenttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ExpensePaymenttypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ExpensePaymenttypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ExpensePaymenttypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpensePaymenttypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpensePaymenttypesIdEndpoint: The initialized ExpensePaymenttypesIdEndpoint object.
        """
        child = ExpensePaymenttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PaymentType]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PaymentType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PaymentType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PaymentType]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PaymentType]: The parsed response data.
        """
        return self._parse_many(PaymentType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PaymentType:
        """
        Performs a POST request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaymentType: The parsed response data.
        """
        return self._parse_one(PaymentType, super()._make_request("POST", data=data, params=params).json())
