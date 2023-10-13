from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsCountEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint import \
    FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TaxableExpenseTypeLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxableExpenseTypeLevel], ConnectWiseManageRequestParams],
    IPostable[TaxableExpenseTypeLevel, ConnectWiseManageRequestParams],
    IPaginateable[TaxableExpenseTypeLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "taxableExpenseTypeLevels", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TaxableExpenseTypeLevel])
        IPostable.__init__(self, TaxableExpenseTypeLevel)
        IPaginateable.__init__(self, TaxableExpenseTypeLevel)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint: The initialized FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdExpensetypeexemptionsIdTaxableexpensetypelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxableExpenseTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/expenseTypeExemptions/{id}/taxableExpenseTypeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableExpenseTypeLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableExpenseTypeLevel, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TaxableExpenseTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/expenseTypeExemptions/{id}/taxableExpenseTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableExpenseTypeLevel]: The parsed response data.
        """
        return self._parse_many(TaxableExpenseTypeLevel, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> TaxableExpenseTypeLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/expenseTypeExemptions/{id}/taxableExpenseTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableExpenseTypeLevel: The parsed response data.
        """
        return self._parse_one(TaxableExpenseTypeLevel, super()._make_request("POST", data=data, params=params).json())
