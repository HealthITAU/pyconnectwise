from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementRmaStatusesIdEndpoint import ProcurementRmaStatusesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaStatusesCountEndpoint import ProcurementRmaStatusesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaStatusesInfoEndpoint import ProcurementRmaStatusesInfoEndpoint
from pyconnectwise.models.manage.RmaStatusModel import RmaStatusModel

class ProcurementRmaStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaStatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRmaStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementRmaStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmaStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmaStatusesIdEndpoint: The initialized ProcurementRmaStatusesIdEndpoint object.
        """
        child = ProcurementRmaStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaStatusModel]:
        """
        Performs a GET request against the /procurement/rmaStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RmaStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaStatusModel]:
        """
        Performs a GET request against the /procurement/rmaStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaStatusModel]: The parsed response data.
        """
        return self._parse_many(RmaStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaStatusModel:
        """
        Performs a POST request against the /procurement/rmaStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatusModel: The parsed response data.
        """
        return self._parse_one(RmaStatusModel, super().make_request("POST", params=params).json())
        