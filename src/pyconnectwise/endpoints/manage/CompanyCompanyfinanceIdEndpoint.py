from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import CompanyFinance
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompanyfinanceIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyFinance:
        """
        Performs a PUT request against the /company/companyFinance/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyFinance: The parsed response data.
        """
        return self._parse_one(CompanyFinance, super()._make_request("PUT", data=data, params=params).json())
