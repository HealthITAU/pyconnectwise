from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsCountEndpoint import (
    FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint import (
    FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import TaxableProductTypeLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxableProductTypeLevel], ConnectWiseManageRequestParams],
    IPostable[TaxableProductTypeLevel, ConnectWiseManageRequestParams],
    IPaginateable[TaxableProductTypeLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "taxableProductTypeLevels", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TaxableProductTypeLevel])
        IPostable.__init__(self, TaxableProductTypeLevel)
        IPaginateable.__init__(self, TaxableProductTypeLevel)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint: The initialized FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdProducttypeexemptionsIdTaxableproducttypelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxableProductTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/productTypeExemptions/{id}/taxableProductTypeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableProductTypeLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxableProductTypeLevel, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TaxableProductTypeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/productTypeExemptions/{id}/taxableProductTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableProductTypeLevel]: The parsed response data.
        """
        return self._parse_many(TaxableProductTypeLevel, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> TaxableProductTypeLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/productTypeExemptions/{id}/taxableProductTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableProductTypeLevel: The parsed response data.
        """
        return self._parse_one(TaxableProductTypeLevel, super()._make_request("POST", data=data, params=params).json())
