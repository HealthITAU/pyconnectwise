from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesIdEndpoint import ProcurementAdjustmentsTypesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesCountEndpoint import ProcurementAdjustmentsTypesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesInfoEndpoint import ProcurementAdjustmentsTypesInfoEndpoint
from pyconnectwise.models.manage.AdjustmentTypeModel import AdjustmentTypeModel

class ProcurementAdjustmentsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementAdjustmentsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementAdjustmentsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementAdjustmentsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementAdjustmentsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementAdjustmentsTypesIdEndpoint: The initialized ProcurementAdjustmentsTypesIdEndpoint object.
        """
        child = ProcurementAdjustmentsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AdjustmentTypeModel]:
        """
        Performs a GET request against the /procurement/adjustments/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdjustmentTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AdjustmentTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AdjustmentTypeModel]:
        """
        Performs a GET request against the /procurement/adjustments/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdjustmentTypeModel]: The parsed response data.
        """
        return self._parse_many(AdjustmentTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AdjustmentTypeModel:
        """
        Performs a POST request against the /procurement/adjustments/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentTypeModel: The parsed response data.
        """
        return self._parse_one(AdjustmentTypeModel, super().make_request("POST", params=params).json())
        