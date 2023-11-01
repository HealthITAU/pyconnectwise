from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypesCountEndpoint import (
    FinanceAgreementtypesIdWorktypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypesIdEndpoint import (
    FinanceAgreementtypesIdWorktypesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AgreementTypeWorkType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAgreementtypesIdWorktypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementTypeWorkType], ConnectWiseManageRequestParams],
    IPostable[AgreementTypeWorkType, ConnectWiseManageRequestParams],
    IPaginateable[AgreementTypeWorkType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "worktypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AgreementTypeWorkType])
        IPostable.__init__(self, AgreementTypeWorkType)
        IPaginateable.__init__(self, AgreementTypeWorkType)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdWorktypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorktypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorktypesIdEndpoint: The initialized FinanceAgreementtypesIdWorktypesIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorktypesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AgreementTypeWorkType]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/worktypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementTypeWorkType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AgreementTypeWorkType]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkType]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeWorkType,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AgreementTypeWorkType:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkType: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeWorkType,
            super()._make_request("POST", data=data, params=params).json(),
        )
