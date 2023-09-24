from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkrolesCountEndpoint import \
    FinanceAgreementsIdWorkrolesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkrolesIdEndpoint import FinanceAgreementsIdWorkrolesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import AgreementWorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAgreementsIdWorkrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementWorkRole], ConnectWiseManageRequestParams],
    IPostable[AgreementWorkRole, ConnectWiseManageRequestParams],
    IPaginateable[AgreementWorkRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workroles", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdWorkrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorkrolesIdEndpoint: The initialized FinanceAgreementsIdWorkrolesIdEndpoint object.
        """
        child = FinanceAgreementsIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[AgreementWorkRole]:
        """
        Performs a GET request against the /finance/agreements/{id}/workroles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementWorkRole, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[AgreementWorkRole]:
        """
        Performs a GET request against the /finance/agreements/{id}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkRole]: The parsed response data.
        """
        return self._parse_many(AgreementWorkRole, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AgreementWorkRole:
        """
        Performs a POST request against the /finance/agreements/{id}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkRole: The parsed response data.
        """
        return self._parse_one(AgreementWorkRole, super()._make_request("POST", data=data, params=params).json())
