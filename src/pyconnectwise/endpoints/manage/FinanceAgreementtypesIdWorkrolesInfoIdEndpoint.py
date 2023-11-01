from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import AgreementTypeWorkRoleInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAgreementtypesIdWorkrolesInfoIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[AgreementTypeWorkRoleInfo, ConnectWiseManageRequestParams],
    IPaginateable[AgreementTypeWorkRoleInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, AgreementTypeWorkRoleInfo)
        IPaginateable.__init__(self, AgreementTypeWorkRoleInfo)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AgreementTypeWorkRoleInfo]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles/info/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRoleInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementTypeWorkRoleInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AgreementTypeWorkRoleInfo:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles/info/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkRoleInfo: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeWorkRoleInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
