from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesetupsCountEndpoint import \
    FinanceInvoicetemplatesetupsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesetupsIdEndpoint import FinanceInvoicetemplatesetupsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import InvoiceTemplateSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceInvoicetemplatesetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[InvoiceTemplateSetup], ConnectWiseManageRequestParams],
    IPaginateable[InvoiceTemplateSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "invoiceTemplateSetups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[InvoiceTemplateSetup])
        IPaginateable.__init__(self, InvoiceTemplateSetup)

        self.count = self._register_child_endpoint(
            FinanceInvoicetemplatesetupsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceInvoicetemplatesetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoicetemplatesetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoicetemplatesetupsIdEndpoint: The initialized FinanceInvoicetemplatesetupsIdEndpoint object.
        """
        child = FinanceInvoicetemplatesetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[InvoiceTemplateSetup]:
        """
        Performs a GET request against the /finance/invoiceTemplateSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceTemplateSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), InvoiceTemplateSetup, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[InvoiceTemplateSetup]:
        """
        Performs a GET request against the /finance/invoiceTemplateSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceTemplateSetup]: The parsed response data.
        """
        return self._parse_many(InvoiceTemplateSetup, super()._make_request("GET", data=data, params=params).json())
