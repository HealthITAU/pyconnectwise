from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeSchedulestopwatchesIdEndpoint import TimeSchedulestopwatchesIdEndpoint
from pyconnectwise.endpoints.manage.TimeSchedulestopwatchesCountEndpoint import TimeSchedulestopwatchesCountEndpoint
from pyconnectwise.models.manage.ScheduleStopwatchModel import ScheduleStopwatchModel

class TimeSchedulestopwatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "schedulestopwatches", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeSchedulestopwatchesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeSchedulestopwatchesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeSchedulestopwatchesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeSchedulestopwatchesIdEndpoint: The initialized TimeSchedulestopwatchesIdEndpoint object.
        """
        child = TimeSchedulestopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleStopwatchModel]:
        """
        Performs a GET request against the /time/schedulestopwatches endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleStopwatchModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleStopwatchModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleStopwatchModel]:
        """
        Performs a GET request against the /time/schedulestopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleStopwatchModel]: The parsed response data.
        """
        return self._parse_many(ScheduleStopwatchModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ScheduleStopwatchModel:
        """
        Performs a POST request against the /time/schedulestopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleStopwatchModel: The parsed response data.
        """
        return self._parse_one(ScheduleStopwatchModel, super().make_request("POST", params=params).json())
        