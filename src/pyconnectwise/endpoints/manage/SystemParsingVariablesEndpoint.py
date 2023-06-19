from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemParsingVariablesIdEndpoint import SystemParsingVariablesIdEndpoint
from pyconnectwise.endpoints.manage.SystemParsingVariablesCountEndpoint import SystemParsingVariablesCountEndpoint
from pyconnectwise.models.manage.ParsingVariableModel import ParsingVariableModel

class SystemParsingVariablesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingVariables", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemParsingVariablesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemParsingVariablesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemParsingVariablesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemParsingVariablesIdEndpoint: The initialized SystemParsingVariablesIdEndpoint object.
        """
        child = SystemParsingVariablesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ParsingVariableModel]:
        """
        Performs a GET request against the /system/parsingVariables endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ParsingVariableModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ParsingVariableModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ParsingVariableModel]:
        """
        Performs a GET request against the /system/parsingVariables endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ParsingVariableModel]: The parsed response data.
        """
        return self._parse_many(ParsingVariableModel, super().make_request("GET", params=params).json())
        