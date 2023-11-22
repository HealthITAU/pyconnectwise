from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesCountEndpoint import SalesActivitiesStatusesCountEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesIdEndpoint import SalesActivitiesStatusesIdEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesInfoEndpoint import SalesActivitiesStatusesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ActivityStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesActivitiesStatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ActivityStatus], ConnectWiseManageRequestParams],
    IPostable[ActivityStatus, ConnectWiseManageRequestParams],
    IPaginateable[ActivityStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "statuses", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ActivityStatus])
        IPostable.__init__(self, ActivityStatus)
        IPaginateable.__init__(self, ActivityStatus)

        self.count = self._register_child_endpoint(SalesActivitiesStatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SalesActivitiesStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SalesActivitiesStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesActivitiesStatusesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SalesActivitiesStatusesIdEndpoint: The initialized SalesActivitiesStatusesIdEndpoint object.
        """
        child = SalesActivitiesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ActivityStatus]:
        """
        Performs a GET request against the /sales/activities/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ActivityStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ActivityStatus, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ActivityStatus]:
        """
        Performs a GET request against the /sales/activities/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityStatus]: The parsed response data.
        """
        return self._parse_many(ActivityStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ActivityStatus:
        """
        Performs a POST request against the /sales/activities/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityStatus: The parsed response data.
        """
        return self._parse_one(ActivityStatus, super()._make_request("POST", data=data, params=params).json())
