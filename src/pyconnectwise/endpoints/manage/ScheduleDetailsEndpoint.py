from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleDetailsCountEndpoint import (
    ScheduleDetailsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleDetailsIdEndpoint import (
    ScheduleDetailsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ScheduleEntryDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ScheduleDetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleEntryDetail], ConnectWiseManageRequestParams],
    IPaginateable[ScheduleEntryDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "details", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ScheduleEntryDetail])
        IPaginateable.__init__(self, ScheduleEntryDetail)

        self.count = self._register_child_endpoint(
            ScheduleDetailsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScheduleDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleDetailsIdEndpoint: The initialized ScheduleDetailsIdEndpoint object.
        """
        child = ScheduleDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ScheduleEntryDetail]:
        """
        Performs a GET request against the /schedule/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleEntryDetail]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScheduleEntryDetail,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ScheduleEntryDetail]:
        """
        Performs a GET request against the /schedule/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleEntryDetail]: The parsed response data.
        """
        return self._parse_many(
            ScheduleEntryDetail,
            super()._make_request("GET", data=data, params=params).json(),
        )
