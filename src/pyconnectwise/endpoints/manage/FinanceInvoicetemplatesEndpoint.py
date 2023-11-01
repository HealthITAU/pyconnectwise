from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesCountEndpoint import (
    FinanceInvoicetemplatesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesIdEndpoint import (
    FinanceInvoicetemplatesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import InvoiceTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceInvoicetemplatesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[InvoiceTemplate], ConnectWiseManageRequestParams],
    IPostable[InvoiceTemplate, ConnectWiseManageRequestParams],
    IPaginateable[InvoiceTemplate, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "invoiceTemplates", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[InvoiceTemplate])
        IPostable.__init__(self, InvoiceTemplate)
        IPaginateable.__init__(self, InvoiceTemplate)

        self.count = self._register_child_endpoint(
            FinanceInvoicetemplatesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceInvoicetemplatesIdEndpoint:  # noqa: A002
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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            InvoiceTemplate,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[InvoiceTemplate]:
        """
        Performs a GET request against the /finance/invoiceTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceTemplate]: The parsed response data.
        """
        return self._parse_many(
            InvoiceTemplate,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> InvoiceTemplate:
        """
        Performs a POST request against the /finance/invoiceTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceTemplate: The parsed response data.
        """
        return self._parse_one(
            InvoiceTemplate,
            super()._make_request("POST", data=data, params=params).json(),
        )
