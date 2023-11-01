from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeTicketstopwatchesCountEndpoint import (
    TimeTicketstopwatchesCountEndpoint,
)
from pyconnectwise.endpoints.manage.TimeTicketstopwatchesIdEndpoint import (
    TimeTicketstopwatchesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import TicketStopwatch
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class TimeTicketstopwatchesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TicketStopwatch], ConnectWiseManageRequestParams],
    IPostable[TicketStopwatch, ConnectWiseManageRequestParams],
    IPaginateable[TicketStopwatch, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "ticketstopwatches", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TicketStopwatch])
        IPostable.__init__(self, TicketStopwatch)
        IPaginateable.__init__(self, TicketStopwatch)

        self.count = self._register_child_endpoint(
            TimeTicketstopwatchesCountEndpoint(client, parent_endpoint=self)
        )

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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TicketStopwatch,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TicketStopwatch]:
        """
        Performs a GET request against the /time/ticketstopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TicketStopwatch]: The parsed response data.
        """
        return self._parse_many(
            TicketStopwatch,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TicketStopwatch:
        """
        Performs a POST request against the /time/ticketstopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketStopwatch: The parsed response data.
        """
        return self._parse_one(
            TicketStopwatch,
            super()._make_request("POST", data=data, params=params).json(),
        )
