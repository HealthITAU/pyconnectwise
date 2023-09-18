from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsCountEndpoint import \
    FinanceAgreementsIdAdditionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsIdEndpoint import FinanceAgreementsIdAdditionsIdEndpoint
from pyconnectwise.models.manage import Addition
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsIdAdditionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "additions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdAdditionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdAdditionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdAdditionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdAdditionsIdEndpoint: The initialized FinanceAgreementsIdAdditionsIdEndpoint object.
        """
        child = FinanceAgreementsIdAdditionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Addition]:
        """
        Performs a GET request against the /finance/agreements/{id}/additions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Addition]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Addition, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Addition]:
        """
        Performs a GET request against the /finance/agreements/{id}/additions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Addition]: The parsed response data.
        """
        return self._parse_many(Addition, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Addition:
        """
        Performs a POST request against the /finance/agreements/{id}/additions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Addition: The parsed response data.
        """
        return self._parse_one(Addition, super()._make_request("POST", data=data, params=params).json())
