from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemParsingvariablesCountEndpoint import SystemParsingvariablesCountEndpoint
from pyconnectwise.endpoints.manage.SystemParsingvariablesIdEndpoint import SystemParsingvariablesIdEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import ParsingVariable
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemParsingvariablesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingVariables", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemParsingvariablesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemParsingvariablesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemParsingvariablesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemParsingvariablesIdEndpoint: The initialized SystemParsingvariablesIdEndpoint object.
        """
        child = SystemParsingvariablesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ParsingVariable]:
        """
        Performs a GET request against the /system/parsingVariables endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ParsingVariable]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ParsingVariable,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ParsingVariable]:
        """
        Performs a GET request against the /system/parsingVariables endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ParsingVariable]: The parsed response data.
        """
        return self._parse_many(ParsingVariable, super()._make_request("GET", data=data, params=params).json())