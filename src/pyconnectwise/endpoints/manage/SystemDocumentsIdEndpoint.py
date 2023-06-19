from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemDocumentsIdDownloadEndpoint import SystemDocumentsIdDownloadEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsIdThumbnailEndpoint import SystemDocumentsIdThumbnailEndpoint
from pyconnectwise.models.manage.DocumentInfoModel import DocumentInfoModel

class SystemDocumentsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.download = self.register_child_endpoint(
            SystemDocumentsIdDownloadEndpoint(client, parent_endpoint=self)
        )
        self.thumbnail = self.register_child_endpoint(
            SystemDocumentsIdThumbnailEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[DocumentInfoModel]:
        """
        Performs a GET request against the /system/documents/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DocumentInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            DocumentInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DocumentInfoModel:
        """
        Performs a GET request against the /system/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentInfoModel: The parsed response data.
        """
        return self._parse_one(DocumentInfoModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /system/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DocumentInfoModel:
        """
        Performs a POST request against the /system/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentInfoModel: The parsed response data.
        """
        return self._parse_one(DocumentInfoModel, super().make_request("POST", params=params).json())
        