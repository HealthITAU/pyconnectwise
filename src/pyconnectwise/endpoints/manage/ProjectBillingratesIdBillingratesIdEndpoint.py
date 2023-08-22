from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import ProjectBillingRate
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectBillingratesIdBillingratesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBillingRate:
        """
        Performs a PATCH request against the /project/billingRates/{id}/billingRates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBillingRate: The parsed response data.
        """
        return self._parse_one(ProjectBillingRate, super()._make_request("PATCH", data=data, params=params).json())
