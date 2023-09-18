from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesCountEndpoint import SalesActivitiesCountEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesIdEndpoint import SalesActivitiesIdEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesStatusesEndpoint import SalesActivitiesStatusesEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesTypesEndpoint import SalesActivitiesTypesEndpoint
from pyconnectwise.models.manage import Activity
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesActivitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "activities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesActivitiesCountEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(SalesActivitiesStatusesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(SalesActivitiesTypesEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesActivitiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesActivitiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesActivitiesIdEndpoint: The initialized SalesActivitiesIdEndpoint object.
        """
        child = SalesActivitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Activity]:
        """
        Performs a GET request against the /sales/activities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Activity]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Activity, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Activity]:
        """
        Performs a GET request against the /sales/activities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Activity]: The parsed response data.
        """
        return self._parse_many(Activity, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Activity:
        """
        Performs a POST request against the /sales/activities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Activity: The parsed response data.
        """
        return self._parse_one(Activity, super()._make_request("POST", data=data, params=params).json())
