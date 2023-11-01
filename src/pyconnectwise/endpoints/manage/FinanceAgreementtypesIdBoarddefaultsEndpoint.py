from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdBoarddefaultsCountEndpoint import (
    FinanceAgreementtypesIdBoarddefaultsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdBoarddefaultsIdEndpoint import (
    FinanceAgreementtypesIdBoarddefaultsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import AgreementTypeBoardDefault
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceAgreementtypesIdBoarddefaultsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementTypeBoardDefault], ConnectWiseManageRequestParams],
    IPostable[AgreementTypeBoardDefault, ConnectWiseManageRequestParams],
    IPaginateable[AgreementTypeBoardDefault, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "boardDefaults", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AgreementTypeBoardDefault])
        IPostable.__init__(self, AgreementTypeBoardDefault)
        IPaginateable.__init__(self, AgreementTypeBoardDefault)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdBoarddefaultsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> FinanceAgreementtypesIdBoarddefaultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdBoarddefaultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdBoarddefaultsIdEndpoint: The initialized FinanceAgreementtypesIdBoarddefaultsIdEndpoint object.
        """
        child = FinanceAgreementtypesIdBoarddefaultsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AgreementTypeBoardDefault]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/boardDefaults endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeBoardDefault]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementTypeBoardDefault,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AgreementTypeBoardDefault]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeBoardDefault]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeBoardDefault,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AgreementTypeBoardDefault:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeBoardDefault: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeBoardDefault,
            super()._make_request("POST", data=data, params=params).json(),
        )
