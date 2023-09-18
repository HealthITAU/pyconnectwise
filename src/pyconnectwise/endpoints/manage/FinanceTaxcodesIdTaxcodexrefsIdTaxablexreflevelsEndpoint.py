from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsCountEndpoint import \
    FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint import \
    FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint
from pyconnectwise.models.manage import TaxableXRefLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableXRefLevels", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint: The initialized FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxableXRefLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs/{id}/taxableXRefLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableXRefLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableXRefLevel, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableXRefLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs/{id}/taxableXRefLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableXRefLevel]: The parsed response data.
        """
        return self._parse_many(TaxableXRefLevel, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableXRefLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/taxCodeXRefs/{id}/taxableXRefLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableXRefLevel: The parsed response data.
        """
        return self._parse_one(TaxableXRefLevel, super()._make_request("POST", data=data, params=params).json())
