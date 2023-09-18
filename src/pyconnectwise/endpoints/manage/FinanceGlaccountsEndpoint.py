from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceGlaccountsCountEndpoint import FinanceGlaccountsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceGlaccountsIdEndpoint import FinanceGlaccountsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceGlaccountsMappedtypesEndpoint import FinanceGlaccountsMappedtypesEndpoint
from pyconnectwise.models.manage import GLAccount
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceGlaccountsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glAccounts", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceGlaccountsCountEndpoint(client, parent_endpoint=self))
        self.mapped_types = self._register_child_endpoint(
            FinanceGlaccountsMappedtypesEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceGlaccountsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceGlaccountsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceGlaccountsIdEndpoint: The initialized FinanceGlaccountsIdEndpoint object.
        """
        child = FinanceGlaccountsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GLAccount]:
        """
        Performs a GET request against the /finance/glAccounts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLAccount]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), GLAccount, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[GLAccount]:
        """
        Performs a GET request against the /finance/glAccounts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GLAccount]: The parsed response data.
        """
        return self._parse_many(GLAccount, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GLAccount:
        """
        Performs a POST request against the /finance/glAccounts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLAccount: The parsed response data.
        """
        return self._parse_one(GLAccount, super()._make_request("POST", data=data, params=params).json())
