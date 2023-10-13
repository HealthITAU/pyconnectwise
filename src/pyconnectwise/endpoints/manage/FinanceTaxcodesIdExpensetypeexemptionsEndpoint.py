from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsCountEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ExpenseTypeExemption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceTaxcodesIdExpensetypeexemptionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ExpenseTypeExemption], ConnectWiseManageRequestParams],
    IPostable[ExpenseTypeExemption, ConnectWiseManageRequestParams],
    IPaginateable[ExpenseTypeExemption, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "expenseTypeExemptions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ExpenseTypeExemption])
        IPostable.__init__(self, ExpenseTypeExemption)
        IPaginateable.__init__(self, ExpenseTypeExemption)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdExpensetypeexemptionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint: The initialized FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint object.
        """
        child = FinanceTaxcodesIdExpensetypeexemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ExpenseTypeExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/expenseTypeExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseTypeExemption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ExpenseTypeExemption, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ExpenseTypeExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/expenseTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseTypeExemption]: The parsed response data.
        """
        return self._parse_many(ExpenseTypeExemption, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ExpenseTypeExemption:
        """
        Performs a POST request against the /finance/taxCodes/{id}/expenseTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseTypeExemption: The parsed response data.
        """
        return self._parse_one(ExpenseTypeExemption, super()._make_request("POST", data=data, params=params).json())
