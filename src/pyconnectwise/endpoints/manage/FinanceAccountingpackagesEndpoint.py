from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesCountEndpoint import (
    FinanceAccountingpackagesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesIdEndpoint import (
    FinanceAccountingpackagesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import AccountingPackage
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAccountingpackagesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AccountingPackage], ConnectWiseManageRequestParams],
    IPaginateable[AccountingPackage, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "accountingPackages", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AccountingPackage])
        IPaginateable.__init__(self, AccountingPackage)

        self.count = self._register_child_endpoint(
            FinanceAccountingpackagesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingpackagesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingpackagesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingpackagesIdEndpoint: The initialized FinanceAccountingpackagesIdEndpoint object.
        """
        child = FinanceAccountingpackagesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AccountingPackage]:
        """
        Performs a GET request against the /finance/accountingPackages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingPackage]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AccountingPackage,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AccountingPackage]:
        """
        Performs a GET request against the /finance/accountingPackages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingPackage]: The parsed response data.
        """
        return self._parse_many(
            AccountingPackage,
            super()._make_request("GET", data=data, params=params).json(),
        )
