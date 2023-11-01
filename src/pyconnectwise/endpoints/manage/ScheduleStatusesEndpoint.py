from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleStatusesCountEndpoint import (
    ScheduleStatusesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleStatusesIdEndpoint import (
    ScheduleStatusesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ScheduleStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ScheduleStatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleStatus], ConnectWiseManageRequestParams],
    IPostable[ScheduleStatus, ConnectWiseManageRequestParams],
    IPaginateable[ScheduleStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "statuses", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ScheduleStatus])
        IPostable.__init__(self, ScheduleStatus)
        IPaginateable.__init__(self, ScheduleStatus)

        self.count = self._register_child_endpoint(
            ScheduleStatusesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScheduleStatusesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ScheduleStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleStatusesIdEndpoint: The initialized ScheduleStatusesIdEndpoint object.
        """
        child = ScheduleStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ScheduleStatus]:
        """
        Performs a GET request against the /schedule/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScheduleStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ScheduleStatus]:
        """
        Performs a GET request against the /schedule/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleStatus]: The parsed response data.
        """
        return self._parse_many(
            ScheduleStatus,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ScheduleStatus:
        """
        Performs a POST request against the /schedule/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleStatus: The parsed response data.
        """
        return self._parse_one(
            ScheduleStatus,
            super()._make_request("POST", data=data, params=params).json(),
        )
