from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeTimeperiodsetupsIdPeriodsCountEndpoint import \
    TimeTimeperiodsetupsIdPeriodsCountEndpoint
from pyconnectwise.endpoints.manage.TimeTimeperiodsetupsIdPeriodsIdEndpoint import \
    TimeTimeperiodsetupsIdPeriodsIdEndpoint
from pyconnectwise.models.manage import TimePeriod
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeTimeperiodsetupsIdPeriodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "periods", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            TimeTimeperiodsetupsIdPeriodsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> TimeTimeperiodsetupsIdPeriodsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeTimeperiodsetupsIdPeriodsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeTimeperiodsetupsIdPeriodsIdEndpoint: The initialized TimeTimeperiodsetupsIdPeriodsIdEndpoint object.
        """
        child = TimeTimeperiodsetupsIdPeriodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimePeriod]:
        """
        Performs a GET request against the /time/timePeriodSetups/{id}/periods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimePeriod]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), TimePeriod, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimePeriod]:
        """
        Performs a GET request against the /time/timePeriodSetups/{id}/periods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimePeriod]: The parsed response data.
        """
        return self._parse_many(TimePeriod, super()._make_request("GET", data=data, params=params).json())
