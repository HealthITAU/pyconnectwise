from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdInfoEndpoint import CompanyConfigurationsTypesIdInfoEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdUsagesEndpoint import CompanyConfigurationsTypesIdUsagesEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsEndpoint import CompanyConfigurationsTypesIdQuestionsEndpoint
from pyconnectwise.models.manage.ConfigurationTypeModel import ConfigurationTypeModel

class CompanyConfigurationsTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            CompanyConfigurationsTypesIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyConfigurationsTypesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.questions = self.register_child_endpoint(
            CompanyConfigurationsTypesIdQuestionsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ConfigurationTypeModel]:
        """
        Performs a GET request against the /company/configurations/types/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ConfigurationTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationTypeModel:
        """
        Performs a GET request against the /company/configurations/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeModel: The parsed response data.
        """
        return self._parse_one(ConfigurationTypeModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/configurations/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationTypeModel:
        """
        Performs a PUT request against the /company/configurations/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeModel: The parsed response data.
        """
        return self._parse_one(ConfigurationTypeModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationTypeModel:
        """
        Performs a PATCH request against the /company/configurations/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeModel: The parsed response data.
        """
        return self._parse_one(ConfigurationTypeModel, super().make_request("PATCH", params=params).json())
        