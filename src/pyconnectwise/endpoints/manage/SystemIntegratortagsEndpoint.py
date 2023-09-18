from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratortagsCountEndpoint import SystemIntegratortagsCountEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratortagsIdEndpoint import SystemIntegratortagsIdEndpoint
from pyconnectwise.models.manage import IntegratorTag
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemIntegratortagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "integratorTags", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemIntegratortagsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemIntegratortagsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemIntegratortagsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemIntegratortagsIdEndpoint: The initialized SystemIntegratortagsIdEndpoint object.
        """
        child = SystemIntegratortagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[IntegratorTag]:
        """
        Performs a GET request against the /system/integratorTags endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[IntegratorTag]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), IntegratorTag, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[IntegratorTag]:
        """
        Performs a GET request against the /system/integratorTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[IntegratorTag]: The parsed response data.
        """
        return self._parse_many(IntegratorTag, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> IntegratorTag:
        """
        Performs a POST request against the /system/integratorTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IntegratorTag: The parsed response data.
        """
        return self._parse_one(IntegratorTag, super()._make_request("POST", data=data, params=params).json())
