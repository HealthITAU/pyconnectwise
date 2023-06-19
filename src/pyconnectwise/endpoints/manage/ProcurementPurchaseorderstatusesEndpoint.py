from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdEndpoint import ProcurementPurchaseorderstatusesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesCountEndpoint import ProcurementPurchaseorderstatusesCountEndpoint
from pyconnectwise.models.manage.PurchaseOrderStatusModel import PurchaseOrderStatusModel

class ProcurementPurchaseorderstatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "purchaseorderstatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPurchaseorderstatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseorderstatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseorderstatusesIdEndpoint: The initialized ProcurementPurchaseorderstatusesIdEndpoint object.
        """
        child = ProcurementPurchaseorderstatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PurchaseOrderStatusModel]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PurchaseOrderStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PurchaseOrderStatusModel]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrderStatusModel]: The parsed response data.
        """
        return self._parse_many(PurchaseOrderStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderStatusModel:
        """
        Performs a POST request against the /procurement/purchaseorderstatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatusModel: The parsed response data.
        """
        return self._parse_one(PurchaseOrderStatusModel, super().make_request("POST", params=params).json())
        