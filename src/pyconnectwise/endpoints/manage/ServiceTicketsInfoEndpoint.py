from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsInfoCountEndpoint import ServiceTicketsInfoCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TicketInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceTicketsInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TicketInfo], ConnectWiseManageRequestParams],
    IPaginateable[TicketInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TicketInfo])
        IPaginateable.__init__(self, TicketInfo)

        self.count = self._register_child_endpoint(ServiceTicketsInfoCountEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TicketInfo]:
        """
        Performs a GET request against the /service/tickets/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TicketInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), TicketInfo, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[TicketInfo]:
        """
        Performs a GET request against the /service/tickets/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TicketInfo]: The parsed response data.
        """
        return self._parse_many(TicketInfo, super()._make_request("GET", data=data, params=params).json())
