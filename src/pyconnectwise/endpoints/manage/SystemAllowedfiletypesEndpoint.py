from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.AllowedFileTypeModel import AllowedFileTypeModel

class SystemAllowedFileTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
    
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AllowedFileTypeModel:
        """
        Performs a POST request against the /system/AllowedFileTypes/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AllowedFileTypeModel: The parsed response data.
        """
        return self._parse_one(AllowedFileTypeModel, super().make_request("POST", params=params).json())
        