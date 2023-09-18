from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesCountEndpoint import SystemInouttypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesIdEndpoint import SystemInouttypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesInfoEndpoint import SystemInouttypesInfoEndpoint
from pyconnectwise.models.manage import InOutType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInouttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inOutTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemInouttypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemInouttypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInouttypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInouttypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInouttypesIdEndpoint: The initialized SystemInouttypesIdEndpoint object.
        """
        child = SystemInouttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InOutType]:
        """
        Performs a GET request against the /system/inOutTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InOutType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), InOutType, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InOutType]:
        """
        Performs a GET request against the /system/inOutTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InOutType]: The parsed response data.
        """
        return self._parse_many(InOutType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InOutType:
        """
        Performs a POST request against the /system/inOutTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InOutType: The parsed response data.
        """
        return self._parse_one(InOutType, super()._make_request("POST", data=data, params=params).json())
