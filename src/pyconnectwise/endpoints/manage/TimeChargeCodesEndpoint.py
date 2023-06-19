from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeChargeCodesIdEndpoint import TimeChargeCodesIdEndpoint
from pyconnectwise.endpoints.manage.TimeChargeCodesCountEndpoint import TimeChargeCodesCountEndpoint
from pyconnectwise.endpoints.manage.TimeChargeCodesInfoEndpoint import TimeChargeCodesInfoEndpoint
from pyconnectwise.models.manage.ChargeCodeModel import ChargeCodeModel

class TimeChargeCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "chargeCodes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeChargeCodesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            TimeChargeCodesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeChargeCodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeChargeCodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeChargeCodesIdEndpoint: The initialized TimeChargeCodesIdEndpoint object.
        """
        child = TimeChargeCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ChargeCodeModel]:
        """
        Performs a GET request against the /time/chargeCodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChargeCodeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ChargeCodeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ChargeCodeModel]:
        """
        Performs a GET request against the /time/chargeCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChargeCodeModel]: The parsed response data.
        """
        return self._parse_many(ChargeCodeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ChargeCodeModel:
        """
        Performs a POST request against the /time/chargeCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChargeCodeModel: The parsed response data.
        """
        return self._parse_one(ChargeCodeModel, super().make_request("POST", params=params).json())
        