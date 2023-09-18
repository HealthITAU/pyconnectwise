from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdScheduleentriesCountEndpoint import \
    ServiceTicketsIdScheduleentriesCountEndpoint
from pyconnectwise.models.manage import ScheduleEntryReference
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTicketsIdScheduleentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "scheduleentries", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ServiceTicketsIdScheduleentriesCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ScheduleEntryReference]:
        """
        Performs a GET request against the /service/tickets/{id}/scheduleentries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleEntryReference]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ScheduleEntryReference, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleEntryReference]:
        """
        Performs a GET request against the /service/tickets/{id}/scheduleentries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleEntryReference]: The parsed response data.
        """
        return self._parse_many(ScheduleEntryReference, super()._make_request("GET", data=data, params=params).json())
