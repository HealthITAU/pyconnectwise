from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesCountEndpoint import TimeEntriesCountEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesDefaultsEndpoint import TimeEntriesDefaultsEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesIdEndpoint import TimeEntriesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TimeEntry
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class TimeEntriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TimeEntry], ConnectWiseManageRequestParams],
    IPostable[TimeEntry, ConnectWiseManageRequestParams],
    IPaginateable[TimeEntry, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "entries", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TimeEntry])
        IPostable.__init__(self, TimeEntry)
        IPaginateable.__init__(self, TimeEntry)

        self.count = self._register_child_endpoint(TimeEntriesCountEndpoint(client, parent_endpoint=self))
        self.defaults = self._register_child_endpoint(TimeEntriesDefaultsEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeEntriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeEntriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeEntriesIdEndpoint: The initialized TimeEntriesIdEndpoint object.
        """
        child = TimeEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TimeEntry]:
        """
        Performs a GET request against the /time/entries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeEntry]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), TimeEntry, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[TimeEntry]:
        """
        Performs a GET request against the /time/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeEntry]: The parsed response data.
        """
        return self._parse_many(TimeEntry, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TimeEntry:
        """
        Performs a POST request against the /time/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeEntry: The parsed response data.
        """
        return self._parse_one(TimeEntry, super()._make_request("POST", data=data, params=params).json())
