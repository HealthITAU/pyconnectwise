from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsCountEndpoint import \
    FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint import \
    FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint
from pyconnectwise.models.manage import TaxableWorkRoleLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableWorkRoleLevels", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint: The initialized FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxableWorkRoleLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableWorkRoleLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableWorkRoleLevel, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableWorkRoleLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableWorkRoleLevel]: The parsed response data.
        """
        return self._parse_many(TaxableWorkRoleLevel, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableWorkRoleLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableWorkRoleLevel: The parsed response data.
        """
        return self._parse_one(TaxableWorkRoleLevel, super()._make_request("POST", data=data, params=params).json())
