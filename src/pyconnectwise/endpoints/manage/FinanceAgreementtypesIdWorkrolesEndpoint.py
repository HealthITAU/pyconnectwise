from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesCountEndpoint import (
    FinanceAgreementtypesIdWorkrolesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesIdEndpoint import (
    FinanceAgreementtypesIdWorkrolesIdEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesInfoEndpoint import (
    FinanceAgreementtypesIdWorkrolesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AgreementTypeWorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAgreementtypesIdWorkrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementTypeWorkRole], ConnectWiseManageRequestParams],
    IPostable[AgreementTypeWorkRole, ConnectWiseManageRequestParams],
    IPaginateable[AgreementTypeWorkRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "workroles", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AgreementTypeWorkRole])
        IPostable.__init__(self, AgreementTypeWorkRole)
        IPaginateable.__init__(self, AgreementTypeWorkRole)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdWorkrolesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorkrolesIdEndpoint: The initialized FinanceAgreementtypesIdWorkrolesIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorkrolesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AgreementTypeWorkRole]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementTypeWorkRole,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AgreementTypeWorkRole]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRole]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeWorkRole,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AgreementTypeWorkRole:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkRole: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeWorkRole,
            super()._make_request("POST", data=data, params=params).json(),
        )
