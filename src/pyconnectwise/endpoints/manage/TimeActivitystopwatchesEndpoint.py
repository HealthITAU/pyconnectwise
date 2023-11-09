from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeActivitystopwatchesCountEndpoint import TimeActivitystopwatchesCountEndpoint
from pyconnectwise.endpoints.manage.TimeActivitystopwatchesIdEndpoint import TimeActivitystopwatchesIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ActivityStopwatch
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class TimeActivitystopwatchesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ActivityStopwatch], ConnectWiseManageRequestParams],
    IPostable[ActivityStopwatch, ConnectWiseManageRequestParams],
    IPaginateable[ActivityStopwatch, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "activitystopwatches", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ActivityStopwatch])
        IPostable.__init__(self, ActivityStopwatch)
        IPaginateable.__init__(self, ActivityStopwatch)

        self.count = self._register_child_endpoint(TimeActivitystopwatchesCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> TimeActivitystopwatchesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeActivitystopwatchesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            TimeActivitystopwatchesIdEndpoint: The initialized TimeActivitystopwatchesIdEndpoint object.
        """
        child = TimeActivitystopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ActivityStopwatch]:
        """
        Performs a GET request against the /time/activitystopwatches endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ActivityStopwatch]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ActivityStopwatch, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ActivityStopwatch]:
        """
        Performs a GET request against the /time/activitystopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityStopwatch]: The parsed response data.
        """
        return self._parse_many(ActivityStopwatch, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ActivityStopwatch:
        """
        Performs a POST request against the /time/activitystopwatches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityStopwatch: The parsed response data.
        """
        return self._parse_one(ActivityStopwatch, super()._make_request("POST", data=data, params=params).json())
