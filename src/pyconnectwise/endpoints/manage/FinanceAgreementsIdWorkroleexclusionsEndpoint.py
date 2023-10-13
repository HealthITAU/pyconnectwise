from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkroleexclusionsCountEndpoint import \
    FinanceAgreementsIdWorkroleexclusionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkroleexclusionsIdEndpoint import \
    FinanceAgreementsIdWorkroleexclusionsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import AgreementWorkRoleExclusion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAgreementsIdWorkroleexclusionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementWorkRoleExclusion], ConnectWiseManageRequestParams],
    IPostable[AgreementWorkRoleExclusion, ConnectWiseManageRequestParams],
    IPaginateable[AgreementWorkRoleExclusion, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "workRoleExclusions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[AgreementWorkRoleExclusion])
        IPostable.__init__(self, AgreementWorkRoleExclusion)
        IPaginateable.__init__(self, AgreementWorkRoleExclusion)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdWorkroleexclusionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdWorkroleexclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorkroleexclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorkroleexclusionsIdEndpoint: The initialized FinanceAgreementsIdWorkroleexclusionsIdEndpoint object.
        """
        child = FinanceAgreementsIdWorkroleexclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[AgreementWorkRoleExclusion]:
        """
        Performs a GET request against the /finance/agreements/{id}/workRoleExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkRoleExclusion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementWorkRoleExclusion, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[AgreementWorkRoleExclusion]:
        """
        Performs a GET request against the /finance/agreements/{id}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkRoleExclusion]: The parsed response data.
        """
        return self._parse_many(
            AgreementWorkRoleExclusion, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> AgreementWorkRoleExclusion:
        """
        Performs a POST request against the /finance/agreements/{id}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkRoleExclusion: The parsed response data.
        """
        return self._parse_one(
            AgreementWorkRoleExclusion, super()._make_request("POST", data=data, params=params).json()
        )
