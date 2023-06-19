from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeActivitystopwatchesIdEndpoint import TimeActivitystopwatchesIdEndpoint
from pyconnectwise.endpoints.manage.TimeActivitystopwatchesCountEndpoint import TimeActivitystopwatchesCountEndpoint
from pyconnectwise.models.manage.ActivityStopwatchModel import ActivityStopwatchModel

class TimeActivitystopwatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "activitystopwatches", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeActivitystopwatchesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeActivitystopwatchesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeActivitystopwatchesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeActivitystopwatchesIdEndpoint: The initialized TimeActivitystopwatchesIdEndpoint object.
        """
        child = TimeActivitystopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ActivityStopwatchModel]:
        """
        Performs a GET request against the /time/activitystopwatches endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ActivityStopwatchModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ActivityStopwatchModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ActivityStopwatchModel]:
        """
        Performs a GET request against the /time/activitystopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityStopwatchModel]: The parsed response data.
        """
        return self._parse_many(ActivityStopwatchModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ActivityStopwatchModel:
        """
        Performs a POST request against the /time/activitystopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityStopwatchModel: The parsed response data.
        """
        return self._parse_one(ActivityStopwatchModel, super().make_request("POST", params=params).json())
        