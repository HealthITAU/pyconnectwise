from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeWorktypesCountEndpoint import TimeWorktypesCountEndpoint
from pyconnectwise.endpoints.manage.TimeWorktypesIdEndpoint import TimeWorktypesIdEndpoint
from pyconnectwise.endpoints.manage.TimeWorktypesInfoEndpoint import TimeWorktypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import WorkType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class TimeWorktypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkType], ConnectWiseManageRequestParams],
    IPostable[WorkType, ConnectWiseManageRequestParams],
    IPaginateable[WorkType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "workTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[WorkType])
        IPostable.__init__(self, WorkType)
        IPaginateable.__init__(self, WorkType)

        self.count = self._register_child_endpoint(TimeWorktypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(TimeWorktypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeWorktypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeWorktypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeWorktypesIdEndpoint: The initialized TimeWorktypesIdEndpoint object.
        """
        child = TimeWorktypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkType]:
        """
        Performs a GET request against the /time/workTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), WorkType, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[WorkType]:
        """
        Performs a GET request against the /time/workTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkType]: The parsed response data.
        """
        return self._parse_many(WorkType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> WorkType:
        """
        Performs a POST request against the /time/workTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkType: The parsed response data.
        """
        return self._parse_one(WorkType, super()._make_request("POST", data=data, params=params).json())
