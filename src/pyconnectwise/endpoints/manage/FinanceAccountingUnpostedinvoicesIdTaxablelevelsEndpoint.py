from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesIdTaxablelevelsCountEndpoint import (
    FinanceAccountingUnpostedinvoicesIdTaxablelevelsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint import (
    FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import UnpostedInvoiceTaxableLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAccountingUnpostedinvoicesIdTaxablelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UnpostedInvoiceTaxableLevel], ConnectWiseManageRequestParams],
    IPaginateable[UnpostedInvoiceTaxableLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "taxableLevels", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[UnpostedInvoiceTaxableLevel])
        IPaginateable.__init__(self, UnpostedInvoiceTaxableLevel)

        self.count = self._register_child_endpoint(
            FinanceAccountingUnpostedinvoicesIdTaxablelevelsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint: The initialized FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint object.
        """
        child = FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[UnpostedInvoiceTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices/{id}/taxableLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedInvoiceTaxableLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UnpostedInvoiceTaxableLevel,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[UnpostedInvoiceTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices/{id}/taxableLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedInvoiceTaxableLevel]: The parsed response data.
        """
        return self._parse_many(
            UnpostedInvoiceTaxableLevel,
            super()._make_request("GET", data=data, params=params).json(),
        )
