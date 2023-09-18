from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxintegrationsCountEndpoint import FinanceTaxintegrationsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxintegrationsIdEndpoint import FinanceTaxintegrationsIdEndpoint
from pyconnectwise.models.manage import TaxIntegration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxintegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxIntegrations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceTaxintegrationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceTaxintegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxintegrationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxintegrationsIdEndpoint: The initialized FinanceTaxintegrationsIdEndpoint object.
        """
        child = FinanceTaxintegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TaxIntegration]:
        """
        Performs a GET request against the /finance/taxIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxIntegration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxIntegration, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxIntegration]:
        """
        Performs a GET request against the /finance/taxIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxIntegration]: The parsed response data.
        """
        return self._parse_many(TaxIntegration, super()._make_request("GET", data=data, params=params).json())
