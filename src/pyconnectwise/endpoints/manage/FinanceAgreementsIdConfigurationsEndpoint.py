from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdConfigurationsIdEndpoint import FinanceAgreementsIdConfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdConfigurationsCountEndpoint import FinanceAgreementsIdConfigurationsCountEndpoint
from pyconnectwise.models.manage.ConfigurationReferenceModel import ConfigurationReferenceModel

class FinanceAgreementsIdConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "configurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdConfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdConfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdConfigurationsIdEndpoint: The initialized FinanceAgreementsIdConfigurationsIdEndpoint object.
        """
        child = FinanceAgreementsIdConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ConfigurationReferenceModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/configurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationReferenceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ConfigurationReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationReferenceModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationReferenceModel]: The parsed response data.
        """
        return self._parse_many(ConfigurationReferenceModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationReferenceModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationReferenceModel: The parsed response data.
        """
        return self._parse_one(ConfigurationReferenceModel, super().make_request("POST", params=params).json())
        