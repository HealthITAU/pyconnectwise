from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemInfoStandardNotesIdEndpoint import SystemInfoStandardNotesIdEndpoint
from pyconnectwise.endpoints.manage.SystemInfoStandardNotesCountEndpoint import SystemInfoStandardNotesCountEndpoint
from pyconnectwise.models.manage.StandardNoteInfoModel import StandardNoteInfoModel

class SystemInfoStandardNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "standardNotes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoStandardNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemInfoStandardNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoStandardNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoStandardNotesIdEndpoint: The initialized SystemInfoStandardNotesIdEndpoint object.
        """
        child = SystemInfoStandardNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[StandardNoteInfoModel]:
        """
        Performs a GET request against the /system/info/standardNotes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[StandardNoteInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            StandardNoteInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[StandardNoteInfoModel]:
        """
        Performs a GET request against the /system/info/standardNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StandardNoteInfoModel]: The parsed response data.
        """
        return self._parse_many(StandardNoteInfoModel, super().make_request("GET", params=params).json())
        