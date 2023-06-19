from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint import FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkTypeExclusionsCountEndpoint import FinanceAgreementTypesIdWorkTypeExclusionsCountEndpoint
from pyconnectwise.models.manage.AgreementTypeWorkTypeExclusionModel import AgreementTypeWorkTypeExclusionModel

class FinanceAgreementTypesIdWorkTypeExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workTypeExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkTypeExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint: The initialized FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint object.
        """
        child = FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeWorkTypeExclusionModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workTypeExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkTypeExclusionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeWorkTypeExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkTypeExclusionModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkTypeExclusionModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkTypeExclusionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkTypeExclusionModel:
        """
        Performs a POST request against the /finance/agreementTypes/{parentId}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkTypeExclusionModel: The parsed response data.
        """
        return self._parse_one(AgreementTypeWorkTypeExclusionModel, super().make_request("POST", params=params).json())
        