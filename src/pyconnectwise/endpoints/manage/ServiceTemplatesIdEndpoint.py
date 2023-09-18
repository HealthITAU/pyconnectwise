from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesIdGenerateEndpoint import ServiceTemplatesIdGenerateEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesIdInfoEndpoint import ServiceTemplatesIdInfoEndpoint
from pyconnectwise.models.manage import ServiceTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTemplatesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.generate = self._register_child_endpoint(ServiceTemplatesIdGenerateEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceTemplatesIdInfoEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ServiceTemplate]:
        """
        Performs a GET request against the /service/templates/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTemplate]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceTemplate, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceTemplate:
        """
        Performs a GET request against the /service/templates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceTemplate: The parsed response data.
        """
        return self._parse_one(ServiceTemplate, super()._make_request("GET", data=data, params=params).json())
