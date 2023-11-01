from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceemailtemplatesCountEndpoint import (
    FinanceInvoiceemailtemplatesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceInvoiceemailtemplatesIdEndpoint import (
    FinanceInvoiceemailtemplatesIdEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceInvoiceemailtemplatesInfoEndpoint import (
    FinanceInvoiceemailtemplatesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import InvoiceEmailTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceInvoiceemailtemplatesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[InvoiceEmailTemplate], ConnectWiseManageRequestParams],
    IPostable[InvoiceEmailTemplate, ConnectWiseManageRequestParams],
    IPaginateable[InvoiceEmailTemplate, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "invoiceEmailTemplates", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[InvoiceEmailTemplate])
        IPostable.__init__(self, InvoiceEmailTemplate)
        IPaginateable.__init__(self, InvoiceEmailTemplate)

        self.count = self._register_child_endpoint(
            FinanceInvoiceemailtemplatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            FinanceInvoiceemailtemplatesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceInvoiceemailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoiceemailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoiceemailtemplatesIdEndpoint: The initialized FinanceInvoiceemailtemplatesIdEndpoint object.
        """
        child = FinanceInvoiceemailtemplatesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[InvoiceEmailTemplate]:
        """
        Performs a GET request against the /finance/invoiceEmailTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceEmailTemplate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            InvoiceEmailTemplate,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[InvoiceEmailTemplate]:
        """
        Performs a GET request against the /finance/invoiceEmailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceEmailTemplate]: The parsed response data.
        """
        return self._parse_many(
            InvoiceEmailTemplate,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> InvoiceEmailTemplate:
        """
        Performs a POST request against the /finance/invoiceEmailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceEmailTemplate: The parsed response data.
        """
        return self._parse_one(
            InvoiceEmailTemplate,
            super()._make_request("POST", data=data, params=params).json(),
        )
