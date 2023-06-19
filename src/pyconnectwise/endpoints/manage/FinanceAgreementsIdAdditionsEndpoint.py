from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsIdEndpoint import FinanceAgreementsIdAdditionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsCountEndpoint import FinanceAgreementsIdAdditionsCountEndpoint
from pyconnectwise.models.manage.AdditionModel import AdditionModel

class FinanceAgreementsIdAdditionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "additions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdAdditionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdAdditionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdAdditionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdAdditionsIdEndpoint: The initialized FinanceAgreementsIdAdditionsIdEndpoint object.
        """
        child = FinanceAgreementsIdAdditionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AdditionModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/additions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdditionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AdditionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AdditionModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/additions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdditionModel]: The parsed response data.
        """
        return self._parse_many(AdditionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AdditionModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/additions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdditionModel: The parsed response data.
        """
        return self._parse_one(AdditionModel, super().make_request("POST", params=params).json())
        