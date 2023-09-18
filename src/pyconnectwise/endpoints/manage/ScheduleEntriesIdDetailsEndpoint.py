from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleEntriesIdDetailsCountEndpoint import ScheduleEntriesIdDetailsCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleEntriesIdDetailsIdEndpoint import ScheduleEntriesIdDetailsIdEndpoint
from pyconnectwise.models.manage import ScheduleDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleEntriesIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ScheduleDetail, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleDetail]:
        """
        Performs a GET request against the /schedule/entries/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleDetail]: The parsed response data.
        """
        return self._parse_many(ScheduleDetail, super()._make_request("GET", data=data, params=params).json())
