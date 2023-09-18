from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeTimeperiodsetupsCountEndpoint import TimeTimeperiodsetupsCountEndpoint
from pyconnectwise.endpoints.manage.TimeTimeperiodsetupsDefaultEndpoint import TimeTimeperiodsetupsDefaultEndpoint
from pyconnectwise.endpoints.manage.TimeTimeperiodsetupsIdEndpoint import TimeTimeperiodsetupsIdEndpoint
from pyconnectwise.models.manage import TimePeriodSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeTimeperiodsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timePeriodSetups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(TimeTimeperiodsetupsCountEndpoint(client, parent_endpoint=self))
        self.default = self._register_child_endpoint(TimeTimeperiodsetupsDefaultEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeTimeperiodsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeTimeperiodsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeTimeperiodsetupsIdEndpoint: The initialized TimeTimeperiodsetupsIdEndpoint object.
        """
        child = TimeTimeperiodsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TimePeriodSetup]:
        """
        Performs a GET request against the /time/timePeriodSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimePeriodSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimePeriodSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimePeriodSetup]:
        """
        Performs a GET request against the /time/timePeriodSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimePeriodSetup]: The parsed response data.
        """
        return self._parse_many(TimePeriodSetup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimePeriodSetup:
        """
        Performs a POST request against the /time/timePeriodSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimePeriodSetup: The parsed response data.
        """
        return self._parse_one(TimePeriodSetup, super()._make_request("POST", data=data, params=params).json())
