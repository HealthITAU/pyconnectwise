from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkRoleExclusionsIdEndpoint import FinanceAgreementsIdWorkRoleExclusionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkRoleExclusionsCountEndpoint import FinanceAgreementsIdWorkRoleExclusionsCountEndpoint
from pyconnectwise.models.manage.AgreementWorkRoleExclusionModel import AgreementWorkRoleExclusionModel

class FinanceAgreementsIdWorkRoleExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorkRoleExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdWorkRoleExclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorkRoleExclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorkRoleExclusionsIdEndpoint: The initialized FinanceAgreementsIdWorkRoleExclusionsIdEndpoint object.
        """
        child = FinanceAgreementsIdWorkRoleExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementWorkRoleExclusionModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/workRoleExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkRoleExclusionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementWorkRoleExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementWorkRoleExclusionModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkRoleExclusionModel]: The parsed response data.
        """
        return self._parse_many(AgreementWorkRoleExclusionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementWorkRoleExclusionModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkRoleExclusionModel: The parsed response data.
        """
        return self._parse_one(AgreementWorkRoleExclusionModel, super().make_request("POST", params=params).json())
        