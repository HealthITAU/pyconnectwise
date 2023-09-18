from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsCountEndpoint import FinanceAgreementsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdEndpoint import FinanceAgreementsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesEndpoint import FinanceAgreementsTypesEndpoint
from pyconnectwise.models.manage import Agreement
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "agreements", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceAgreementsCountEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(FinanceAgreementsTypesEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceAgreementsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdEndpoint: The initialized FinanceAgreementsIdEndpoint object.
        """
        child = FinanceAgreementsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Agreement]:
        """
        Performs a GET request against the /finance/agreements endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Agreement]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Agreement, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Agreement]:
        """
        Performs a GET request against the /finance/agreements endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Agreement]: The parsed response data.
        """
        return self._parse_many(Agreement, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Agreement:
        """
        Performs a POST request against the /finance/agreements endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Agreement: The parsed response data.
        """
        return self._parse_one(Agreement, super()._make_request("POST", data=data, params=params).json())
