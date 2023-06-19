from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdValuesInfoCountEndpoint import ConfigurationsTypesIdQuestionsIdValuesInfoCountEndpoint
from pyconnectwise.models.manage.ConfigurationTypeQuestionValueInfoModel import ConfigurationTypeQuestionValueInfoModel

class ConfigurationsTypesIdQuestionsIdValuesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdValuesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ConfigurationTypeQuestionValueInfoModel]:
        """
        Performs a GET request against the /configurations/types/{grandparentId}/questions/{parentId}/values/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestionValueInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ConfigurationTypeQuestionValueInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationTypeQuestionValueInfoModel]:
        """
        Performs a GET request against the /configurations/types/{grandparentId}/questions/{parentId}/values/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestionValueInfoModel]: The parsed response data.
        """
        return self._parse_many(ConfigurationTypeQuestionValueInfoModel, super().make_request("GET", params=params).json())
        