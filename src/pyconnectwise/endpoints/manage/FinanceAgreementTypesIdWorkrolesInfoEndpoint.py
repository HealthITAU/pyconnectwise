from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkrolesInfoIdEndpoint import FinanceAgreementTypesIdWorkrolesInfoIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkrolesInfoCountEndpoint import FinanceAgreementTypesIdWorkrolesInfoCountEndpoint
from pyconnectwise.models.manage.AgreementTypeWorkRoleInfoModel import AgreementTypeWorkRoleInfoModel

class FinanceAgreementTypesIdWorkrolesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkrolesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkrolesInfoIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementTypesIdWorkrolesInfoIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementTypesIdWorkrolesInfoIdEndpoint: The initialized FinanceAgreementTypesIdWorkrolesInfoIdEndpoint object.
        """
        child = FinanceAgreementTypesIdWorkrolesInfoIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeWorkRoleInfoModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workroles/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRoleInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeWorkRoleInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkRoleInfoModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workroles/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRoleInfoModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkRoleInfoModel, super().make_request("GET", params=params).json())
        