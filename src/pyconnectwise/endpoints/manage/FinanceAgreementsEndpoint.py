from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsCountEndpoint import (
    FinanceAgreementsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdEndpoint import (
    FinanceAgreementsIdEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesEndpoint import (
    FinanceAgreementsTypesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import Agreement
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAgreementsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Agreement], ConnectWiseManageRequestParams],
    IPostable[Agreement, ConnectWiseManageRequestParams],
    IPaginateable[Agreement, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "agreements", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Agreement])
        IPostable.__init__(self, Agreement)
        IPaginateable.__init__(self, Agreement)

        self.count = self._register_child_endpoint(
            FinanceAgreementsCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self._register_child_endpoint(
            FinanceAgreementsTypesEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdEndpoint: The initialized FinanceAgreementsIdEndpoint object.
        """
        child = FinanceAgreementsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Agreement]:
        """
        Performs a GET request against the /finance/agreements endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Agreement]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Agreement,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Agreement]:
        """
        Performs a GET request against the /finance/agreements endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Agreement]: The parsed response data.
        """
        return self._parse_many(
            Agreement, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Agreement:
        """
        Performs a POST request against the /finance/agreements endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Agreement: The parsed response data.
        """
        return self._parse_one(
            Agreement, super()._make_request("POST", data=data, params=params).json()
        )
