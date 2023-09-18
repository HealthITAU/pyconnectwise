from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesCountEndpoint import ScheduleTypesCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesIdEndpoint import ScheduleTypesIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesInfoEndpoint import ScheduleTypesInfoEndpoint
from pyconnectwise.models.manage import ScheduleType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ScheduleTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ScheduleTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ScheduleTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleTypesIdEndpoint: The initialized ScheduleTypesIdEndpoint object.
        """
        child = ScheduleTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ScheduleType]:
        """
        Performs a GET request against the /schedule/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ScheduleType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleType]:
        """
        Performs a GET request against the /schedule/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleType]: The parsed response data.
        """
        return self._parse_many(ScheduleType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ScheduleType:
        """
        Performs a POST request against the /schedule/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleType: The parsed response data.
        """
        return self._parse_one(ScheduleType, super()._make_request("POST", data=data, params=params).json())
