from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesCountEndpoint import SalesActivitiesStatusesCountEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesIdEndpoint import SalesActivitiesStatusesIdEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesInfoEndpoint import SalesActivitiesStatusesInfoEndpoint
from pyconnectwise.models.manage import ActivityStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesActivitiesStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesActivitiesStatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SalesActivitiesStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesActivitiesStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesActivitiesStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesActivitiesStatusesIdEndpoint: The initialized SalesActivitiesStatusesIdEndpoint object.
        """
        child = SalesActivitiesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ActivityStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ActivityStatus]:
        """
        Performs a GET request against the /sales/activities/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityStatus]: The parsed response data.
        """
        return self._parse_many(ActivityStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ActivityStatus:
        """
        Performs a POST request against the /sales/activities/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityStatus: The parsed response data.
        """
        return self._parse_one(ActivityStatus, super()._make_request("POST", data=data, params=params).json())
