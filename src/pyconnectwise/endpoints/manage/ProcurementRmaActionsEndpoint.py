from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementRmaActionsIdEndpoint import ProcurementRmaActionsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaActionsCountEndpoint import ProcurementRmaActionsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaActionsInfoEndpoint import ProcurementRmaActionsInfoEndpoint
from pyconnectwise.models.manage.RmaActionModel import RmaActionModel

class ProcurementRmaActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaActions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaActionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRmaActionsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementRmaActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmaActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmaActionsIdEndpoint: The initialized ProcurementRmaActionsIdEndpoint object.
        """
        child = ProcurementRmaActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaActionModel]:
        """
        Performs a GET request against the /procurement/rmaActions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaActionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RmaActionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaActionModel]:
        """
        Performs a GET request against the /procurement/rmaActions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaActionModel]: The parsed response data.
        """
        return self._parse_many(RmaActionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaActionModel:
        """
        Performs a POST request against the /procurement/rmaActions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaActionModel: The parsed response data.
        """
        return self._parse_one(RmaActionModel, super().make_request("POST", params=params).json())
        