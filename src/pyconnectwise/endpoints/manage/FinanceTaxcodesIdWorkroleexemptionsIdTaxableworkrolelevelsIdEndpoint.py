from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import TaxableWorkRoleLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxableWorkRoleLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableWorkRoleLevel:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableWorkRoleLevel: The parsed response data.
        """
        return self._parse_one(TaxableWorkRoleLevel, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableWorkRoleLevel:
        """
        Performs a PUT request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableWorkRoleLevel: The parsed response data.
        """
        return self._parse_one(TaxableWorkRoleLevel, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableWorkRoleLevel:
        """
        Performs a PATCH request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableWorkRoleLevel: The parsed response data.
        """
        return self._parse_one(TaxableWorkRoleLevel, super()._make_request("PATCH", data=data, params=params).json())
