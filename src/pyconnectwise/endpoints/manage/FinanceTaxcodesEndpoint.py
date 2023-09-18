from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesCountEndpoint import FinanceTaxcodesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdEndpoint import FinanceTaxcodesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesInfoEndpoint import FinanceTaxcodesInfoEndpoint
from pyconnectwise.models.manage import TaxCode
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceTaxcodesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(FinanceTaxcodesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceTaxcodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdEndpoint: The initialized FinanceTaxcodesIdEndpoint object.
        """
        child = FinanceTaxcodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxCode]:
        """
        Performs a GET request against the /finance/taxCodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCode]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), TaxCode, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxCode]:
        """
        Performs a GET request against the /finance/taxCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCode]: The parsed response data.
        """
        return self._parse_many(TaxCode, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCode:
        """
        Performs a POST request against the /finance/taxCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCode: The parsed response data.
        """
        return self._parse_one(TaxCode, super()._make_request("POST", data=data, params=params).json())
