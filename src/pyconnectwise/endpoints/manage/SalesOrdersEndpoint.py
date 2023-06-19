from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOrdersIdEndpoint import SalesOrdersIdEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersCountEndpoint import SalesOrdersCountEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesEndpoint import SalesOrdersStatusesEndpoint
from pyconnectwise.models.manage.OrderModel import OrderModel

class SalesOrdersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "orders", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            SalesOrdersStatusesEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOrdersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOrdersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOrdersIdEndpoint: The initialized SalesOrdersIdEndpoint object.
        """
        child = SalesOrdersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OrderModel]:
        """
        Performs a GET request against the /sales/orders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OrderModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderModel]:
        """
        Performs a GET request against the /sales/orders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderModel]: The parsed response data.
        """
        return self._parse_many(OrderModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OrderModel:
        """
        Performs a POST request against the /sales/orders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderModel: The parsed response data.
        """
        return self._parse_one(OrderModel, super().make_request("POST", params=params).json())
        