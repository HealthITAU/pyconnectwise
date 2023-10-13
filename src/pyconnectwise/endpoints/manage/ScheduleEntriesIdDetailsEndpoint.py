from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleEntriesIdDetailsCountEndpoint import ScheduleEntriesIdDetailsCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleEntriesIdDetailsIdEndpoint import ScheduleEntriesIdDetailsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ScheduleDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScheduleEntriesIdDetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleDetail], ConnectWiseManageRequestParams],
    IPaginateable[ScheduleDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "details", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ScheduleDetail])
        IPaginateable.__init__(self, ScheduleDetail)

        self.count = self._register_child_endpoint(ScheduleEntriesIdDetailsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ScheduleEntriesIdDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleEntriesIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleEntriesIdDetailsIdEndpoint: The initialized ScheduleEntriesIdDetailsIdEndpoint object.
        """
        child = ScheduleEntriesIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ScheduleDetail]:
        """
        Performs a GET request against the /schedule/entries/{id}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleDetail]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ScheduleDetail, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ScheduleDetail]:
        """
        Performs a GET request against the /schedule/entries/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleDetail]: The parsed response data.
        """
        return self._parse_many(ScheduleDetail, super()._make_request("GET", data=data, params=params).json())
