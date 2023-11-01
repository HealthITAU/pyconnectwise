from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsCountEndpoint import (
    FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint import (
    FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import TaxableWorkRoleLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxableWorkRoleLevel], ConnectWiseManageRequestParams],
    IPostable[TaxableWorkRoleLevel, ConnectWiseManageRequestParams],
    IPaginateable[TaxableWorkRoleLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "taxableWorkRoleLevels", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TaxableWorkRoleLevel])
        IPostable.__init__(self, TaxableWorkRoleLevel)
        IPaginateable.__init__(self, TaxableWorkRoleLevel)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint: The initialized FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint object.
        """
        child = FinanceTaxcodesIdWorkroleexemptionsIdTaxableworkrolelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TaxableWorkRoleLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableWorkRoleLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TaxableWorkRoleLevel,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TaxableWorkRoleLevel]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableWorkRoleLevel]: The parsed response data.
        """
        return self._parse_many(
            TaxableWorkRoleLevel,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TaxableWorkRoleLevel:
        """
        Performs a POST request against the /finance/taxCodes/{id}/workRoleExemptions/{id}/taxableWorkRoleLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableWorkRoleLevel: The parsed response data.
        """
        return self._parse_one(
            TaxableWorkRoleLevel,
            super()._make_request("POST", data=data, params=params).json(),
        )
