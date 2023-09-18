from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsCountEndpoint import ProcurementAdjustmentsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsIdEndpoint import ProcurementAdjustmentsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsTypesEndpoint import ProcurementAdjustmentsTypesEndpoint
from pyconnectwise.models.manage import ProcurementAdjustment
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementAdjustmentsCountEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(ProcurementAdjustmentsTypesEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementAdjustmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementAdjustmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementAdjustmentsIdEndpoint: The initialized ProcurementAdjustmentsIdEndpoint object.
        """
        child = ProcurementAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProcurementAdjustment]:
        """
        Performs a GET request against the /procurement/adjustments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProcurementAdjustment]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProcurementAdjustment, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProcurementAdjustment]:
        """
        Performs a GET request against the /procurement/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProcurementAdjustment]: The parsed response data.
        """
        return self._parse_many(ProcurementAdjustment, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProcurementAdjustment:
        """
        Performs a POST request against the /procurement/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProcurementAdjustment: The parsed response data.
        """
        return self._parse_one(ProcurementAdjustment, super()._make_request("POST", data=data, params=params).json())
