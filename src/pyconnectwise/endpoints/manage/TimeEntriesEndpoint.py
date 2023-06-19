from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeEntriesIdEndpoint import TimeEntriesIdEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesCountEndpoint import TimeEntriesCountEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesDefaultsEndpoint import TimeEntriesDefaultsEndpoint
from pyconnectwise.models.manage.TimeEntryModel import TimeEntryModel

class TimeEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeEntriesCountEndpoint(client, parent_endpoint=self)
        )
        self.defaults = self.register_child_endpoint(
            TimeEntriesDefaultsEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeEntriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeEntriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeEntriesIdEndpoint: The initialized TimeEntriesIdEndpoint object.
        """
        child = TimeEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeEntryModel]:
        """
        Performs a GET request against the /time/entries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeEntryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimeEntryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeEntryModel]:
        """
        Performs a GET request against the /time/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeEntryModel]: The parsed response data.
        """
        return self._parse_many(TimeEntryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeEntryModel:
        """
        Performs a POST request against the /time/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeEntryModel: The parsed response data.
        """
        return self._parse_one(TimeEntryModel, super().make_request("POST", params=params).json())
        