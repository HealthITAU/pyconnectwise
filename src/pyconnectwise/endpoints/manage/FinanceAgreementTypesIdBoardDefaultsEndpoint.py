from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdBoardDefaultsIdEndpoint import FinanceAgreementTypesIdBoardDefaultsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdBoardDefaultsCountEndpoint import FinanceAgreementTypesIdBoardDefaultsCountEndpoint
from pyconnectwise.models.manage.AgreementTypeBoardDefaultModel import AgreementTypeBoardDefaultModel

class FinanceAgreementTypesIdBoardDefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardDefaults", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdBoardDefaultsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementTypesIdBoardDefaultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementTypesIdBoardDefaultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementTypesIdBoardDefaultsIdEndpoint: The initialized FinanceAgreementTypesIdBoardDefaultsIdEndpoint object.
        """
        child = FinanceAgreementTypesIdBoardDefaultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeBoardDefaultModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/boardDefaults endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeBoardDefaultModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeBoardDefaultModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeBoardDefaultModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeBoardDefaultModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeBoardDefaultModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeBoardDefaultModel:
        """
        Performs a POST request against the /finance/agreementTypes/{parentId}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeBoardDefaultModel: The parsed response data.
        """
        return self._parse_one(AgreementTypeBoardDefaultModel, super().make_request("POST", params=params).json())
        