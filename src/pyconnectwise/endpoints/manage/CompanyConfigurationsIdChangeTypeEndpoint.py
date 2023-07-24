from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import Company
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyConfigurationsIdChangetypeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "changeType", parent_endpoint=parent_endpoint)

    def patch(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> Company:
        """
        Performs a PATCH request against the /company/configurations/{id}/changeType endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Company: The parsed response data.
        """
        return self._parse_one(
            Company, super()._make_request("PATCH", data=data, params=params).json()
        )
