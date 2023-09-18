from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodelevelsCountEndpoint import \
    FinanceTaxcodesIdTaxcodelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodelevelsIdEndpoint import \
    FinanceTaxcodesIdTaxcodelevelsIdEndpoint
from pyconnectwise.models.manage import TaxCodeLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdTaxcodelevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodeLevels", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdTaxcodelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdTaxcodelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdTaxcodelevelsIdEndpoint: The initialized FinanceTaxcodesIdTaxcodelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdTaxcodelevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxCodeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxCodeLevel, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxCodeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCodeLevel]: The parsed response data.
        """
        return self._parse_many(TaxCodeLevel, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/taxCodeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeLevel: The parsed response data.
        """
        return self._parse_one(TaxCodeLevel, super()._make_request("POST", data=data, params=params).json())
