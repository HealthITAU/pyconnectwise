from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesIdEndpoint import CompanyConfigurationsStatusesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesCountEndpoint import CompanyConfigurationsStatusesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsStatusesInfoEndpoint import CompanyConfigurationsStatusesInfoEndpoint
from pyconnectwise.models.manage.ConfigurationStatusModel import ConfigurationStatusModel

class CompanyConfigurationsStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyConfigurationsStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyConfigurationsStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyConfigurationsStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyConfigurationsStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyConfigurationsStatusesIdEndpoint: The initialized CompanyConfigurationsStatusesIdEndpoint object.
        """
        child = CompanyConfigurationsStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ConfigurationStatusModel]:
        """
        Performs a GET request against the /company/configurations/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ConfigurationStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationStatusModel]:
        """
        Performs a GET request against the /company/configurations/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationStatusModel]: The parsed response data.
        """
        return self._parse_many(ConfigurationStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationStatusModel:
        """
        Performs a POST request against the /company/configurations/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationStatusModel: The parsed response data.
        """
        return self._parse_one(ConfigurationStatusModel, super().make_request("POST", params=params).json())
        