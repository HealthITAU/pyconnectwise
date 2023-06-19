from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkTypeExclusionsIdEndpoint import FinanceAgreementsIdWorkTypeExclusionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkTypeExclusionsCountEndpoint import FinanceAgreementsIdWorkTypeExclusionsCountEndpoint
from pyconnectwise.models.manage.AgreementWorkTypeExclusionModel import AgreementWorkTypeExclusionModel

class FinanceAgreementsIdWorkTypeExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workTypeExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorkTypeExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdWorkTypeExclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorkTypeExclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorkTypeExclusionsIdEndpoint: The initialized FinanceAgreementsIdWorkTypeExclusionsIdEndpoint object.
        """
        child = FinanceAgreementsIdWorkTypeExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementWorkTypeExclusionModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/workTypeExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkTypeExclusionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementWorkTypeExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementWorkTypeExclusionModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkTypeExclusionModel]: The parsed response data.
        """
        return self._parse_many(AgreementWorkTypeExclusionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementWorkTypeExclusionModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkTypeExclusionModel: The parsed response data.
        """
        return self._parse_one(AgreementWorkTypeExclusionModel, super().make_request("POST", params=params).json())
        