from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeSheetsCountEndpoint import TimeSheetsCountEndpoint
from pyconnectwise.endpoints.manage.TimeSheetsIdEndpoint import TimeSheetsIdEndpoint
from pyconnectwise.models.manage import TimeSheet
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeSheetsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sheets", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(TimeSheetsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeSheetsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeSheetsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeSheetsIdEndpoint: The initialized TimeSheetsIdEndpoint object.
        """
        child = TimeSheetsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeSheet]:
        """
        Performs a GET request against the /time/sheets endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeSheet]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), TimeSheet, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeSheet]:
        """
        Performs a GET request against the /time/sheets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeSheet]: The parsed response data.
        """
        return self._parse_many(TimeSheet, super()._make_request("GET", data=data, params=params).json())
