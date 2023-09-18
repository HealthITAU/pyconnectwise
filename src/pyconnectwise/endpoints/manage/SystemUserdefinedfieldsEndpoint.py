from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsCountEndpoint import SystemUserdefinedfieldsCountEndpoint
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsIdEndpoint import SystemUserdefinedfieldsIdEndpoint
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsInfoEndpoint import SystemUserdefinedfieldsInfoEndpoint
from pyconnectwise.models.manage import UserDefinedField
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemUserdefinedfieldsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "userDefinedFields", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemUserdefinedfieldsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemUserdefinedfieldsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemUserdefinedfieldsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemUserdefinedfieldsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemUserdefinedfieldsIdEndpoint: The initialized SystemUserdefinedfieldsIdEndpoint object.
        """
        child = SystemUserdefinedfieldsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[UserDefinedField]:
        """
        Performs a GET request against the /system/userDefinedFields endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UserDefinedField]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), UserDefinedField, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UserDefinedField]:
        """
        Performs a GET request against the /system/userDefinedFields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UserDefinedField]: The parsed response data.
        """
        return self._parse_many(UserDefinedField, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UserDefinedField:
        """
        Performs a POST request against the /system/userDefinedFields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserDefinedField: The parsed response data.
        """
        return self._parse_one(UserDefinedField, super()._make_request("POST", data=data, params=params).json())
