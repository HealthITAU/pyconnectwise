from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TaxIntegration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceTaxintegrationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[TaxIntegration, ConnectWiseManageRequestParams],
    IPuttable[TaxIntegration, ConnectWiseManageRequestParams],
    IPatchable[TaxIntegration, ConnectWiseManageRequestParams],
    IPaginateable[TaxIntegration, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TaxIntegration)
        IPuttable.__init__(self, TaxIntegration)
        IPatchable.__init__(self, TaxIntegration)
        IPaginateable.__init__(self, TaxIntegration)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxIntegration]:
        """
        Performs a GET request against the /finance/taxIntegrations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxIntegration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxIntegration, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TaxIntegration:
        """
        Performs a GET request against the /finance/taxIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxIntegration: The parsed response data.
        """
        return self._parse_one(TaxIntegration, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TaxIntegration:
        """
        Performs a PUT request against the /finance/taxIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxIntegration: The parsed response data.
        """
        return self._parse_one(TaxIntegration, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> TaxIntegration:
        """
        Performs a PATCH request against the /finance/taxIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxIntegration: The parsed response data.
        """
        return self._parse_one(TaxIntegration, super()._make_request("PATCH", data=data, params=params).json())
