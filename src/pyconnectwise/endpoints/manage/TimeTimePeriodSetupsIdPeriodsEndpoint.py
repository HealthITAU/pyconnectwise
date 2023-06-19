from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeTimePeriodSetupsIdPeriodsIdEndpoint import TimeTimePeriodSetupsIdPeriodsIdEndpoint
from pyconnectwise.endpoints.manage.TimeTimePeriodSetupsIdPeriodsCountEndpoint import TimeTimePeriodSetupsIdPeriodsCountEndpoint
from pyconnectwise.models.manage.TimePeriodModel import TimePeriodModel

class TimeTimePeriodSetupsIdPeriodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "periods", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeTimePeriodSetupsIdPeriodsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeTimePeriodSetupsIdPeriodsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeTimePeriodSetupsIdPeriodsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeTimePeriodSetupsIdPeriodsIdEndpoint: The initialized TimeTimePeriodSetupsIdPeriodsIdEndpoint object.
        """
        child = TimeTimePeriodSetupsIdPeriodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimePeriodModel]:
        """
        Performs a GET request against the /time/timePeriodSetups/{parentId}/periods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimePeriodModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimePeriodModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimePeriodModel]:
        """
        Performs a GET request against the /time/timePeriodSetups/{parentId}/periods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimePeriodModel]: The parsed response data.
        """
        return self._parse_many(TimePeriodModel, super().make_request("GET", params=params).json())
        