from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdEndpoint import FinanceAgreementsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsCountEndpoint import FinanceAgreementsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesEndpoint import FinanceAgreementsTypesEndpoint
from pyconnectwise.models.manage.AgreementModel import AgreementModel

class FinanceAgreementsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "agreements", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            FinanceAgreementsTypesEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdEndpoint: The initialized FinanceAgreementsIdEndpoint object.
        """
        child = FinanceAgreementsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementModel]:
        """
        Performs a GET request against the /finance/agreements endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementModel]:
        """
        Performs a GET request against the /finance/agreements endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementModel]: The parsed response data.
        """
        return self._parse_many(AgreementModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementModel:
        """
        Performs a POST request against the /finance/agreements endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementModel: The parsed response data.
        """
        return self._parse_one(AgreementModel, super().make_request("POST", params=params).json())
        