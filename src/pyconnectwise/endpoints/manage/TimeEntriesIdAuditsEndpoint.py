from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesIdAuditsCountEndpoint import TimeEntriesIdAuditsCountEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesIdAuditsIdEndpoint import TimeEntriesIdAuditsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TimeEntryAudit
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class TimeEntriesIdAuditsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TimeEntryAudit], ConnectWiseManageRequestParams],
    IPaginateable[TimeEntryAudit, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "audits", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TimeEntryAudit])
        IPaginateable.__init__(self, TimeEntryAudit)

        self.count = self._register_child_endpoint(TimeEntriesIdAuditsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeEntriesIdAuditsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeEntriesIdAuditsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeEntriesIdAuditsIdEndpoint: The initialized TimeEntriesIdAuditsIdEndpoint object.
        """
        child = TimeEntriesIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TimeEntryAudit]:
        """
        Performs a GET request against the /time/entries/{id}/audits endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeEntryAudit]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimeEntryAudit, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TimeEntryAudit]:
        """
        Performs a GET request against the /time/entries/{id}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeEntryAudit]: The parsed response data.
        """
        return self._parse_many(TimeEntryAudit, super()._make_request("GET", data=data, params=params).json())
