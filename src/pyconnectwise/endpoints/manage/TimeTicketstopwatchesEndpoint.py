from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeTicketstopwatchesCountEndpoint import TimeTicketstopwatchesCountEndpoint
from pyconnectwise.endpoints.manage.TimeTicketstopwatchesIdEndpoint import TimeTicketstopwatchesIdEndpoint
from pyconnectwise.models.manage import TicketStopwatch
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeTicketstopwatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ticketstopwatches", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(TimeTicketstopwatchesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeTicketstopwatchesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeTicketstopwatchesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeTicketstopwatchesIdEndpoint: The initialized TimeTicketstopwatchesIdEndpoint object.
        """
        child = TimeTicketstopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TicketStopwatch]:
        """
        Performs a GET request against the /time/ticketstopwatches endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TicketStopwatch]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TicketStopwatch, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TicketStopwatch]:
        """
        Performs a GET request against the /time/ticketstopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TicketStopwatch]: The parsed response data.
        """
        return self._parse_many(TicketStopwatch, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TicketStopwatch:
        """
        Performs a POST request against the /time/ticketstopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketStopwatch: The parsed response data.
        """
        return self._parse_one(TicketStopwatch, super()._make_request("POST", data=data, params=params).json())
