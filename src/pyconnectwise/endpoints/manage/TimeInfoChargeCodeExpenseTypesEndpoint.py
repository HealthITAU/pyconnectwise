from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeInfoChargeCodeExpenseTypesCountEndpoint import TimeInfoChargeCodeExpenseTypesCountEndpoint
from pyconnectwise.models.manage.ChargeCodeExpenseTypeModel import ChargeCodeExpenseTypeModel

class TimeInfoChargeCodeExpenseTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "chargeCodeExpenseTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeInfoChargeCodeExpenseTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ChargeCodeExpenseTypeModel]:
        """
        Performs a GET request against the /time/info/chargeCodeExpenseTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChargeCodeExpenseTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ChargeCodeExpenseTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ChargeCodeExpenseTypeModel]:
        """
        Performs a GET request against the /time/info/chargeCodeExpenseTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChargeCodeExpenseTypeModel]: The parsed response data.
        """
        return self._parse_many(ChargeCodeExpenseTypeModel, super().make_request("GET", params=params).json())
        