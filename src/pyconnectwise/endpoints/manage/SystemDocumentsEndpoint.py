from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemDocumentsIdEndpoint import SystemDocumentsIdEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsCountEndpoint import SystemDocumentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsUploadsampleEndpoint import SystemDocumentsUploadsampleEndpoint
from pyconnectwise.models.manage.DocumentInfoModel import DocumentInfoModel

class SystemDocumentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documents", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemDocumentsCountEndpoint(client, parent_endpoint=self)
        )
        self.uploadsample = self.register_child_endpoint(
            SystemDocumentsUploadsampleEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemDocumentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemDocumentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemDocumentsIdEndpoint: The initialized SystemDocumentsIdEndpoint object.
        """
        child = SystemDocumentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[DocumentInfoModel]:
        """
        Performs a GET request against the /system/documents endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DocumentInfoModel]:
        """
        Performs a GET request against the /system/documents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DocumentInfoModel]: The parsed response data.
        """
        return self._parse_many(DocumentInfoModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DocumentInfoModel:
        """
        Performs a POST request against the /system/documents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentInfoModel: The parsed response data.
        """
        return self._parse_one(DocumentInfoModel, super().make_request("POST", params=params).json())
        