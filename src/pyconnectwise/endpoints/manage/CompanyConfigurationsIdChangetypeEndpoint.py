from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import CompanyConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyConfigurationsIdChangetypeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "changeType", parent_endpoint=parent_endpoint)

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyConfiguration:
        """
        Performs a PATCH request against the /company/configurations/{id}/changeType endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyConfiguration: The parsed response data.
        """
        return self._parse_one(CompanyConfiguration, super()._make_request("PATCH", data=data, params=params).json())
