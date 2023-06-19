from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEmailtemplatesIdEndpoint import SalesOrdersStatusesIdEmailtemplatesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEmailtemplatesCountEndpoint import SalesOrdersStatusesIdEmailtemplatesCountEndpoint
from pyconnectwise.models.manage.OrderStatusEmailTemplateModel import OrderStatusEmailTemplateModel

class SalesOrdersStatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersStatusesIdEmailtemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOrdersStatusesIdEmailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOrdersStatusesIdEmailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOrdersStatusesIdEmailtemplatesIdEndpoint: The initialized SalesOrdersStatusesIdEmailtemplatesIdEndpoint object.
        """
        child = SalesOrdersStatusesIdEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OrderStatusEmailTemplateModel]:
        """
        Performs a GET request against the /sales/orders/statuses/{parentId}/emailtemplates/ endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatusEmailTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OrderStatusEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatusEmailTemplateModel]:
        """
        Performs a GET request against the /sales/orders/statuses/{parentId}/emailtemplates/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatusEmailTemplateModel]: The parsed response data.
        """
        return self._parse_many(OrderStatusEmailTemplateModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OrderStatusEmailTemplateModel:
        """
        Performs a POST request against the /sales/orders/statuses/{parentId}/emailtemplates/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatusEmailTemplateModel: The parsed response data.
        """
        return self._parse_one(OrderStatusEmailTemplateModel, super().make_request("POST", params=params).json())
        