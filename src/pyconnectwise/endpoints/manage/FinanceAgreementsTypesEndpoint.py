from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesIdEndpoint import FinanceAgreementsTypesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesCountEndpoint import FinanceAgreementsTypesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesInfoEndpoint import FinanceAgreementsTypesInfoEndpoint
from pyconnectwise.models.manage.AgreementTypeModel import AgreementTypeModel

class FinanceAgreementsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceAgreementsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsTypesIdEndpoint: The initialized FinanceAgreementsTypesIdEndpoint object.
        """
        child = FinanceAgreementsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeModel]:
        """
        Performs a GET request against the /finance/agreements/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeModel]:
        """
        Performs a GET request against the /finance/agreements/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeModel:
        """
        Performs a POST request against the /finance/agreements/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeModel: The parsed response data.
        """
        return self._parse_one(AgreementTypeModel, super().make_request("POST", params=params).json())
        