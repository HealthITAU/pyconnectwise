from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesTypesCountEndpoint import SalesActivitiesTypesCountEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesTypesIdEndpoint import SalesActivitiesTypesIdEndpoint
from pyconnectwise.models.manage import ActivityType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesActivitiesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesActivitiesTypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesActivitiesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesActivitiesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesActivitiesTypesIdEndpoint: The initialized SalesActivitiesTypesIdEndpoint object.
        """
        child = SalesActivitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ActivityType]:
        """
        Performs a GET request against the /sales/activities/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ActivityType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ActivityType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ActivityType]:
        """
        Performs a GET request against the /sales/activities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityType]: The parsed response data.
        """
        return self._parse_many(ActivityType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ActivityType:
        """
        Performs a POST request against the /sales/activities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityType: The parsed response data.
        """
        return self._parse_one(ActivityType, super()._make_request("POST", data=data, params=params).json())
