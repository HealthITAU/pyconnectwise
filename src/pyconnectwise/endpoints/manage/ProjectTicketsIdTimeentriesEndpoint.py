from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdTimeentriesCountEndpoint import \
    ProjectTicketsIdTimeentriesCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TimeEntryReference
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectTicketsIdTimeentriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TimeEntryReference], ConnectWiseManageRequestParams],
    IPaginateable[TimeEntryReference, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "timeentries", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TimeEntryReference])
        IPaginateable.__init__(self, TimeEntryReference)

        self.count = self._register_child_endpoint(
            ProjectTicketsIdTimeentriesCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TimeEntryReference]:
        """
        Performs a GET request against the /project/tickets/{id}/timeentries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeEntryReference]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimeEntryReference, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TimeEntryReference]:
        """
        Performs a GET request against the /project/tickets/{id}/timeentries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeEntryReference]: The parsed response data.
        """
        return self._parse_many(TimeEntryReference, super()._make_request("GET", data=data, params=params).json())
