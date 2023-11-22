from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseInfoTaxtypesCountEndpoint import ExpenseInfoTaxtypesCountEndpoint
from pyconnectwise.endpoints.manage.ExpenseInfoTaxtypesIdEndpoint import ExpenseInfoTaxtypesIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import ExpenseTaxTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ExpenseInfoTaxtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ExpenseTaxTypeInfo], ConnectWiseManageRequestParams],
    IPaginateable[ExpenseTaxTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "taxTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ExpenseTaxTypeInfo])
        IPaginateable.__init__(self, ExpenseTaxTypeInfo)

        self.count = self._register_child_endpoint(ExpenseInfoTaxtypesCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ExpenseInfoTaxtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseInfoTaxtypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ExpenseInfoTaxtypesIdEndpoint: The initialized ExpenseInfoTaxtypesIdEndpoint object.
        """
        child = ExpenseInfoTaxtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ExpenseTaxTypeInfo]:
        """
        Performs a GET request against the /expense/info/taxTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseTaxTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ExpenseTaxTypeInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ExpenseTaxTypeInfo]:
        """
        Performs a GET request against the /expense/info/taxTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseTaxTypeInfo]: The parsed response data.
        """
        return self._parse_many(ExpenseTaxTypeInfo, super()._make_request("GET", data=data, params=params).json())
