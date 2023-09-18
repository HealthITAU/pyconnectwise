from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesCountEndpoint import ProcurementRmastatusesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdEndpoint import ProcurementRmastatusesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesInfoEndpoint import ProcurementRmastatusesInfoEndpoint
from pyconnectwise.models.manage import RmaStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementRmastatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaStatuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementRmastatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementRmastatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementRmastatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmastatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmastatusesIdEndpoint: The initialized ProcurementRmastatusesIdEndpoint object.
        """
        child = ProcurementRmastatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaStatus]:
        """
        Performs a GET request against the /procurement/rmaStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), RmaStatus, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaStatus]:
        """
        Performs a GET request against the /procurement/rmaStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaStatus]: The parsed response data.
        """
        return self._parse_many(RmaStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaStatus:
        """
        Performs a POST request against the /procurement/rmaStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("POST", data=data, params=params).json())
