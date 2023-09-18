from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemExperimentsCountEndpoint import SystemExperimentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemExperimentsIdEndpoint import SystemExperimentsIdEndpoint
from pyconnectwise.models.manage import Experiment
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemExperimentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "experiments", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemExperimentsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemExperimentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemExperimentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemExperimentsIdEndpoint: The initialized SystemExperimentsIdEndpoint object.
        """
        child = SystemExperimentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Experiment]:
        """
        Performs a GET request against the /system/experiments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Experiment]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Experiment, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Experiment]:
        """
        Performs a GET request against the /system/experiments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Experiment]: The parsed response data.
        """
        return self._parse_many(Experiment, super()._make_request("GET", data=data, params=params).json())
