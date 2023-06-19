from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesCommissionsIdEndpoint import SalesCommissionsIdEndpoint
from pyconnectwise.endpoints.manage.SalesCommissionsCountEndpoint import SalesCommissionsCountEndpoint
from pyconnectwise.models.manage.CommissionModel import CommissionModel

class SalesCommissionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "commissions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesCommissionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesCommissionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesCommissionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesCommissionsIdEndpoint: The initialized SalesCommissionsIdEndpoint object.
        """
        child = SalesCommissionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CommissionModel]:
        """
        Performs a GET request against the /sales/commissions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CommissionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CommissionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CommissionModel]:
        """
        Performs a GET request against the /sales/commissions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CommissionModel]: The parsed response data.
        """
        return self._parse_many(CommissionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CommissionModel:
        """
        Performs a POST request against the /sales/commissions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommissionModel: The parsed response data.
        """
        return self._parse_one(CommissionModel, super().make_request("POST", params=params).json())
        