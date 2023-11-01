from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodelevelsCountEndpoint import (
    FinanceTaxcodesIdTaxcodelevelsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdTaxcodelevelsIdEndpoint import (
    FinanceTaxcodesIdTaxcodelevelsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import TaxCodeLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceTaxcodesIdTaxcodelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxCodeLevel], ConnectWiseManageRequestParams],
    IPostable[TaxCodeLevel, ConnectWiseManageRequestParams],
    IPaginateable[TaxCodeLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "taxCodeLevels", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TaxCodeLevel])
        IPostable.__init__(self, TaxCodeLevel)
        IPaginateable.__init__(self, TaxCodeLevel)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdTaxcodelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdTaxcodelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdTaxcodelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdTaxcodelevelsIdEndpoint: The initialized FinanceTaxcodesIdTaxcodelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdTaxcodelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TaxCodeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TaxCodeLevel,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TaxCodeLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/taxCodeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCodeLevel]: The parsed response data.
        """
        return self._parse_many(
            TaxCodeLevel, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TaxCodeLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/taxCodeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeLevel: The parsed response data.
        """
        return self._parse_one(
            TaxCodeLevel, super()._make_request("POST", data=data, params=params).json()
        )
