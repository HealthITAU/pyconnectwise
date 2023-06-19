from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemParsingTypesIdEndpoint import SystemParsingTypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemParsingTypesCountEndpoint import SystemParsingTypesCountEndpoint
from pyconnectwise.models.manage.ParsingTypeModel import ParsingTypeModel

class SystemParsingTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemParsingTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemParsingTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemParsingTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemParsingTypesIdEndpoint: The initialized SystemParsingTypesIdEndpoint object.
        """
        child = SystemParsingTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ParsingTypeModel]:
        """
        Performs a GET request against the /system/parsingTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ParsingTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ParsingTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ParsingTypeModel]:
        """
        Performs a GET request against the /system/parsingTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ParsingTypeModel]: The parsed response data.
        """
        return self._parse_many(ParsingTypeModel, super().make_request("GET", params=params).json())
        