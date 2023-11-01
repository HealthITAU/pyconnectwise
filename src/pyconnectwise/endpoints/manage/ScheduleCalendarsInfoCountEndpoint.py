from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import CalendarInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ScheduleCalendarsInfoCountEndpoint(
    ConnectWiseEndpoint,
    IGettable[CalendarInfo, ConnectWiseManageRequestParams],
    IPaginateable[CalendarInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "count", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, CalendarInfo)
        IPaginateable.__init__(self, CalendarInfo)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CalendarInfo]:
        """
        Performs a GET request against the /schedule/calendars/info/count endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CalendarInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CalendarInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CalendarInfo:
        """
        Performs a GET request against the /schedule/calendars/info/count endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CalendarInfo: The parsed response data.
        """
        return self._parse_one(
            CalendarInfo, super()._make_request("GET", data=data, params=params).json()
        )
