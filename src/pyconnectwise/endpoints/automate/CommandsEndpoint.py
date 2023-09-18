from typing import Any

from pyconnectwise.endpoints.automate.CommandsIdEndpoint import CommandsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechCommand
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CommandsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Commands", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> CommandsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CommandsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CommandsIdEndpoint: The initialized CommandsIdEndpoint object.
        """
        child = CommandsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechCommand]:
        """
        Performs a GET request against the /Commands endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechCommand]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechCommand, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechCommand]:
        """
        Performs a GET request against the /Commands endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechCommand]: The parsed response data.
        """
        return self._parse_many(LabTechCommand, super()._make_request("GET", data=data, params=params).json())
