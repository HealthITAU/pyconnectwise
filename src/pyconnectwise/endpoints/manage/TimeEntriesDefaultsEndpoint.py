from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.TimeEntryModel import TimeEntryModel

class TimeEntriesDefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "defaults", parent_endpoint=parent_endpoint)
        
    
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeEntryModel:
        """
        Performs a POST request against the /time/entries/defaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeEntryModel: The parsed response data.
        """
        return self._parse_one(TimeEntryModel, super().make_request("POST", params=params).json())
        