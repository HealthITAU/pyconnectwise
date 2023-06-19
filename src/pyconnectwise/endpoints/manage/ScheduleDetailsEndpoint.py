from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ScheduleDetailsIdEndpoint import ScheduleDetailsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleDetailsCountEndpoint import ScheduleDetailsCountEndpoint
from pyconnectwise.models.manage.ScheduleEntryDetailModel import ScheduleEntryDetailModel

class ScheduleDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ScheduleDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleDetailsIdEndpoint: The initialized ScheduleDetailsIdEndpoint object.
        """
        child = ScheduleDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleEntryDetailModel]:
        """
        Performs a GET request against the /schedule/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleEntryDetailModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleEntryDetailModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleEntryDetailModel]:
        """
        Performs a GET request against the /schedule/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleEntryDetailModel]: The parsed response data.
        """
        return self._parse_many(ScheduleEntryDetailModel, super().make_request("GET", params=params).json())
        