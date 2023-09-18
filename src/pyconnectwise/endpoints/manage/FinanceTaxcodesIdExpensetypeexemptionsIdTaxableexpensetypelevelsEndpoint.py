from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsCountEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint
from pyconnectwise.models.manage import TaxableExpenseTypeLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableExpenseTypeLevels", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint: The initialized FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxableExpenseTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/expenseTypeExemptions/{id}/taxableExpenseTypeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableExpenseTypeLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableExpenseTypeLevel, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableExpenseTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/expenseTypeExemptions/{id}/taxableExpenseTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableExpenseTypeLevel]: The parsed response data.
        """
        return self._parse_many(TaxableExpenseTypeLevel, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableExpenseTypeLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/expenseTypeExemptions/{id}/taxableExpenseTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableExpenseTypeLevel: The parsed response data.
        """
        return self._parse_one(TaxableExpenseTypeLevel, super()._make_request("POST", data=data, params=params).json())
