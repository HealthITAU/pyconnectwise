from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOrdersStatusesInfoCountEndpoint import SalesOrdersStatusesInfoCountEndpoint
from pyconnectwise.models.manage.OrderStatusInfoModel import OrderStatusInfoModel

class SalesOrdersStatusesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersStatusesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OrderStatusInfoModel]:
        """
        Performs a GET request against the /sales/orders/statuses/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatusInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OrderStatusInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatusInfoModel]:
        """
        Performs a GET request against the /sales/orders/statuses/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatusInfoModel]: The parsed response data.
        """
        return self._parse_many(OrderStatusInfoModel, super().make_request("GET", params=params).json())
        