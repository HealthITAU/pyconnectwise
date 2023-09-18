from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsCountEndpoint import \
    FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint import \
    FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint
from pyconnectwise.models.manage import TaxableProductTypeLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableProductTypeLevels", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint: The initialized FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxableProductTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/productTypeExemptions/{id}/taxableProductTypeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableProductTypeLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableProductTypeLevel, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableProductTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/productTypeExemptions/{id}/taxableProductTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableProductTypeLevel]: The parsed response data.
        """
        return self._parse_many(TaxableProductTypeLevel, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableProductTypeLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/productTypeExemptions/{id}/taxableProductTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableProductTypeLevel: The parsed response data.
        """
        return self._parse_one(TaxableProductTypeLevel, super()._make_request("POST", data=data, params=params).json())
