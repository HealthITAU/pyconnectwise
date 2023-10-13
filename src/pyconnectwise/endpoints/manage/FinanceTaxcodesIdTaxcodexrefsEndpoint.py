from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsCountEndpoint import \
    FinanceTaxcodesIdTaxcodexrefsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodexrefsIdEndpoint import \
    FinanceTaxcodesIdTaxcodexrefsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TaxCodeXRef
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceTaxcodesIdTaxcodexrefsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxCodeXRef], ConnectWiseManageRequestParams],
    IPostable[TaxCodeXRef, ConnectWiseManageRequestParams],
    IPaginateable[TaxCodeXRef, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "taxCodeXRefs", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TaxCodeXRef])
        IPostable.__init__(self, TaxCodeXRef)
        IPaginateable.__init__(self, TaxCodeXRef)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodexrefsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdTaxcodexrefsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdTaxcodexrefsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdTaxcodexrefsIdEndpoint: The initialized FinanceTaxcodesIdTaxcodexrefsIdEndpoint object.
        """
        child = FinanceTaxcodesIdTaxcodexrefsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxCodeXRef]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeXRef]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxCodeXRef, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[TaxCodeXRef]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeXRefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCodeXRef]: The parsed response data.
        """
        return self._parse_many(TaxCodeXRef, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TaxCodeXRef:
        """
        Performs a POST request against the /finance/taxCodes/{id}/taxCodeXRefs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeXRef: The parsed response data.
        """
        return self._parse_one(TaxCodeXRef, super()._make_request("POST", data=data, params=params).json())
