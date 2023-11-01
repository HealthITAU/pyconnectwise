from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeSchedulestopwatchesCountEndpoint import (
    TimeSchedulestopwatchesCountEndpoint,
)
from pyconnectwise.endpoints.manage.TimeSchedulestopwatchesIdEndpoint import (
    TimeSchedulestopwatchesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ScheduleStopwatch
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class TimeSchedulestopwatchesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleStopwatch], ConnectWiseManageRequestParams],
    IPostable[ScheduleStopwatch, ConnectWiseManageRequestParams],
    IPaginateable[ScheduleStopwatch, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "schedulestopwatches", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ScheduleStopwatch])
        IPostable.__init__(self, ScheduleStopwatch)
        IPaginateable.__init__(self, ScheduleStopwatch)

        self.count = self._register_child_endpoint(
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

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ScheduleStopwatch]:
        """
        Performs a GET request against the /time/schedulestopwatches endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleStopwatch]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScheduleStopwatch,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ScheduleStopwatch]:
        """
        Performs a GET request against the /time/schedulestopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleStopwatch]: The parsed response data.
        """
        return self._parse_many(
            ScheduleStopwatch,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ScheduleStopwatch:
        """
        Performs a POST request against the /time/schedulestopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleStopwatch: The parsed response data.
        """
        return self._parse_one(
            ScheduleStopwatch,
            super()._make_request("POST", data=data, params=params).json(),
        )
