from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorktypesIdEndpoint import FinanceAgreementTypesIdWorktypesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorktypesCountEndpoint import FinanceAgreementTypesIdWorktypesCountEndpoint
from pyconnectwise.models.manage.AgreementTypeWorkTypeModel import AgreementTypeWorkTypeModel

class FinanceAgreementTypesIdWorktypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "worktypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorktypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorktypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementTypesIdWorktypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementTypesIdWorktypesIdEndpoint: The initialized FinanceAgreementTypesIdWorktypesIdEndpoint object.
        """
        child = FinanceAgreementTypesIdWorktypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeWorkTypeModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/worktypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeWorkTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkTypeModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkTypeModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkTypeModel:
        """
        Performs a POST request against the /finance/agreementTypes/{parentId}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkTypeModel: The parsed response data.
        """
        return self._parse_one(AgreementTypeWorkTypeModel, super().make_request("POST", params=params).json())
        