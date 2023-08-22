from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import TemplateGeneratedCountsModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTemplatesIdGenerateEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "generate", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TemplateGeneratedCountsModel:
        """
        Performs a POST request against the /service/templates/{id}/generate endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TemplateGeneratedCountsModel: The parsed response data.
        """
        return self._parse_one(
            TemplateGeneratedCountsModel, super()._make_request("POST", data=data, params=params).json()
        )
