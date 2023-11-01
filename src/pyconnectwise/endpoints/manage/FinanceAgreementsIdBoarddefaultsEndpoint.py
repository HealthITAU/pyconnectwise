from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoarddefaultsCountEndpoint import (
    FinanceAgreementsIdBoarddefaultsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoarddefaultsIdEndpoint import (
    FinanceAgreementsIdBoarddefaultsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import BoardDefault
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAgreementsIdBoarddefaultsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardDefault], ConnectWiseManageRequestParams],
    IPostable[BoardDefault, ConnectWiseManageRequestParams],
    IPaginateable[BoardDefault, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "boardDefaults", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BoardDefault])
        IPostable.__init__(self, BoardDefault)
        IPaginateable.__init__(self, BoardDefault)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdBoarddefaultsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdBoarddefaultsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdBoarddefaultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdBoarddefaultsIdEndpoint: The initialized FinanceAgreementsIdBoarddefaultsIdEndpoint object.
        """
        child = FinanceAgreementsIdBoarddefaultsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardDefault]:
        """
        Performs a GET request against the /finance/agreements/{id}/boardDefaults endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardDefault]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardDefault,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BoardDefault]:
        """
        Performs a GET request against the /finance/agreements/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardDefault]: The parsed response data.
        """
        return self._parse_many(
            BoardDefault, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardDefault:
        """
        Performs a POST request against the /finance/agreements/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardDefault: The parsed response data.
        """
        return self._parse_one(
            BoardDefault, super()._make_request("POST", data=data, params=params).json()
        )
