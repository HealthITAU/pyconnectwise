from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdSitesIdEndpoint import FinanceAgreementsIdSitesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdSitesCountEndpoint import FinanceAgreementsIdSitesCountEndpoint
from pyconnectwise.models.manage.AgreementSiteModel import AgreementSiteModel

class FinanceAgreementsIdSitesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sites", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdSitesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdSitesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdSitesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdSitesIdEndpoint: The initialized FinanceAgreementsIdSitesIdEndpoint object.
        """
        child = FinanceAgreementsIdSitesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementSiteModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/sites endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementSiteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementSiteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementSiteModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementSiteModel]: The parsed response data.
        """
        return self._parse_many(AgreementSiteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementSiteModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementSiteModel: The parsed response data.
        """
        return self._parse_one(AgreementSiteModel, super().make_request("POST", params=params).json())
        