from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdCopyEndpoint import FinanceTaxcodesIdCopyEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdInfoEndpoint import FinanceTaxcodesIdInfoEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsEndpoint import \
    FinanceTaxcodesIdProducttypeexemptionsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodelevelsEndpoint import FinanceTaxcodesIdTaxcodelevelsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsEndpoint import FinanceTaxcodesIdTaxcodexrefsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdUsagesEndpoint import FinanceTaxcodesIdUsagesEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsEndpoint import \
    FinanceTaxcodesIdWorkroleexemptionsEndpoint
from pyconnectwise.models.manage import TaxCode
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.work_role_exemptions = self._register_child_endpoint(
            FinanceTaxcodesIdWorkroleexemptionsEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(FinanceTaxcodesIdUsagesEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(FinanceTaxcodesIdInfoEndpoint(client, parent_endpoint=self))
        self.tax_code_x_refs = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodexrefsEndpoint(client, parent_endpoint=self)
        )
        self.copy = self._register_child_endpoint(FinanceTaxcodesIdCopyEndpoint(client, parent_endpoint=self))
        self.tax_code_levels = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodelevelsEndpoint(client, parent_endpoint=self)
        )
        self.expense_type_exemptions = self._register_child_endpoint(
            FinanceTaxcodesIdExpensetypeexemptionsEndpoint(client, parent_endpoint=self)
        )
        self.product_type_exemptions = self._register_child_endpoint(
            FinanceTaxcodesIdProducttypeexemptionsEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxCode]:
        """
        Performs a GET request against the /finance/taxCodes/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCode:
        """
        Performs a GET request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCode: The parsed response data.
        """
        return self._parse_one(TaxCode, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCode:
        """
        Performs a PUT request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCode: The parsed response data.
        """
        return self._parse_one(TaxCode, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCode:
        """
        Performs a PATCH request against the /finance/taxCodes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCode: The parsed response data.
        """
        return self._parse_one(TaxCode, super()._make_request("PATCH", data=data, params=params).json())
