from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesCountEndpoint import FinanceInvoicetemplatesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesIdEndpoint import FinanceInvoicetemplatesIdEndpoint
from pyconnectwise.models.manage import InvoiceTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceInvoicetemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceTemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceInvoicetemplatesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceInvoicetemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoicetemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoicetemplatesIdEndpoint: The initialized FinanceInvoicetemplatesIdEndpoint object.
        """
        child = FinanceInvoicetemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[InvoiceTemplate]:
        """
        Performs a GET request against the /finance/invoiceTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceTemplate]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), InvoiceTemplate, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InvoiceTemplate]:
        """
        Performs a GET request against the /finance/invoiceTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceTemplate]: The parsed response data.
        """
        return self._parse_many(InvoiceTemplate, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoiceTemplate:
        """
        Performs a POST request against the /finance/invoiceTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceTemplate: The parsed response data.
        """
        return self._parse_one(InvoiceTemplate, super()._make_request("POST", data=data, params=params).json())
