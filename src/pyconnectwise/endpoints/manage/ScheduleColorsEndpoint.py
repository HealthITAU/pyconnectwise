from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ScheduleColorsIdEndpoint import ScheduleColorsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleColorsCountEndpoint import ScheduleColorsCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleColorsResetEndpoint import ScheduleColorsResetEndpoint
from pyconnectwise.models.manage.ScheduleColorModel import ScheduleColorModel

class ScheduleColorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "colors", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleColorsCountEndpoint(client, parent_endpoint=self)
        )
        self.reset = self.register_child_endpoint(
            ScheduleColorsResetEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ScheduleColorsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleColorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleColorsIdEndpoint: The initialized ScheduleColorsIdEndpoint object.
        """
        child = ScheduleColorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleColorModel]:
        """
        Performs a GET request against the /schedule/colors endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleColorModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleColorModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleColorModel]:
        """
        Performs a GET request against the /schedule/colors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleColorModel]: The parsed response data.
        """
        return self._parse_many(ScheduleColorModel, super().make_request("GET", params=params).json())
        