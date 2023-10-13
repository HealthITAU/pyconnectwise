from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsCountEndpoint import \
    FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint import \
    FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TaxableXRefLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxableXRefLevel], ConnectWiseManageRequestParams],
    IPostable[TaxableXRefLevel, ConnectWiseManageRequestParams],
    IPaginateable[TaxableXRefLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "taxableXRefLevels", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TaxableXRefLevel])
        IPostable.__init__(self, TaxableXRefLevel)
        IPaginateable.__init__(self, TaxableXRefLevel)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint: The initialized FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdTaxcodexrefsIdTaxablexreflevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxableXRefLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs/{id}/taxableXRefLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableXRefLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableXRefLevel, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TaxableXRefLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs/{id}/taxableXRefLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableXRefLevel]: The parsed response data.
        """
        return self._parse_many(TaxableXRefLevel, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TaxableXRefLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/taxCodeXRefs/{id}/taxableXRefLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableXRefLevel: The parsed response data.
        """
        return self._parse_one(TaxableXRefLevel, super()._make_request("POST", data=data, params=params).json())
