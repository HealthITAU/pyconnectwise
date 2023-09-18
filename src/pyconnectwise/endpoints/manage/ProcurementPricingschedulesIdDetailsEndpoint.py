from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsCountEndpoint import \
    ProcurementPricingschedulesIdDetailsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdEndpoint import \
    ProcurementPricingschedulesIdDetailsIdEndpoint
from pyconnectwise.models.manage import PricingDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPricingschedulesIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementPricingschedulesIdDetailsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPricingschedulesIdDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPricingschedulesIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPricingschedulesIdDetailsIdEndpoint: The initialized ProcurementPricingschedulesIdDetailsIdEndpoint object.
        """
        child = ProcurementPricingschedulesIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PricingDetail]:
        """
        Performs a GET request against the /procurement/pricingschedules/{id}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingDetail]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PricingDetail, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PricingDetail]:
        """
        Performs a GET request against the /procurement/pricingschedules/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingDetail]: The parsed response data.
        """
        return self._parse_many(PricingDetail, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PricingDetail:
        """
        Performs a POST request against the /procurement/pricingschedules/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingDetail: The parsed response data.
        """
        return self._parse_one(PricingDetail, super()._make_request("POST", data=data, params=params).json())
