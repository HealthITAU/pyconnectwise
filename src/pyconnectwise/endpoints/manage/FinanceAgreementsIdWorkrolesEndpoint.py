from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkrolesIdEndpoint import FinanceAgreementsIdWorkrolesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkrolesCountEndpoint import FinanceAgreementsIdWorkrolesCountEndpoint
from pyconnectwise.models.manage.AgreementWorkRoleModel import AgreementWorkRoleModel

class FinanceAgreementsIdWorkrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workroles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdWorkrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorkrolesIdEndpoint: The initialized FinanceAgreementsIdWorkrolesIdEndpoint object.
        """
        child = FinanceAgreementsIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementWorkRoleModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/workroles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkRoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementWorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementWorkRoleModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkRoleModel]: The parsed response data.
        """
        return self._parse_many(AgreementWorkRoleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementWorkRoleModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkRoleModel: The parsed response data.
        """
        return self._parse_one(AgreementWorkRoleModel, super().make_request("POST", params=params).json())
        