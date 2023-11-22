from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesCountEndpoint import TimeWorkrolesCountEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdEndpoint import TimeWorkrolesIdEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesInfoEndpoint import TimeWorkrolesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import WorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class TimeWorkrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkRole], ConnectWiseManageRequestParams],
    IPostable[WorkRole, ConnectWiseManageRequestParams],
    IPaginateable[WorkRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "workRoles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[WorkRole])
        IPostable.__init__(self, WorkRole)
        IPaginateable.__init__(self, WorkRole)

        self.count = self._register_child_endpoint(TimeWorkrolesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(TimeWorkrolesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> TimeWorkrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            TimeWorkrolesIdEndpoint: The initialized TimeWorkrolesIdEndpoint object.
        """
        child = TimeWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkRole]:
        """
        Performs a GET request against the /time/workRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), WorkRole, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[WorkRole]:
        """
        Performs a GET request against the /time/workRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRole]: The parsed response data.
        """
        return self._parse_many(WorkRole, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> WorkRole:
        """
        Performs a POST request against the /time/workRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(WorkRole, super()._make_request("POST", data=data, params=params).json())
