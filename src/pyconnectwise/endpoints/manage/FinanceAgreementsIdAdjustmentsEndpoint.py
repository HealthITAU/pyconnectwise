from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdjustmentsIdEndpoint import FinanceAgreementsIdAdjustmentsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdjustmentsCountEndpoint import FinanceAgreementsIdAdjustmentsCountEndpoint
from pyconnectwise.models.manage.AdjustmentModel import AdjustmentModel

class FinanceAgreementsIdAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdAdjustmentsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdAdjustmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdAdjustmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdAdjustmentsIdEndpoint: The initialized FinanceAgreementsIdAdjustmentsIdEndpoint object.
        """
        child = FinanceAgreementsIdAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AdjustmentModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/adjustments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdjustmentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AdjustmentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AdjustmentModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdjustmentModel]: The parsed response data.
        """
        return self._parse_many(AdjustmentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AdjustmentModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentModel: The parsed response data.
        """
        return self._parse_one(AdjustmentModel, super().make_request("POST", params=params).json())
        