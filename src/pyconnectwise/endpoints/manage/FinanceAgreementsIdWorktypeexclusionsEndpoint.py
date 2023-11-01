from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypeexclusionsCountEndpoint import (
    FinanceAgreementsIdWorktypeexclusionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypeexclusionsIdEndpoint import (
    FinanceAgreementsIdWorktypeexclusionsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import AgreementWorkTypeExclusion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceAgreementsIdWorktypeexclusionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementWorkTypeExclusion], ConnectWiseManageRequestParams],
    IPostable[AgreementWorkTypeExclusion, ConnectWiseManageRequestParams],
    IPaginateable[AgreementWorkTypeExclusion, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "workTypeExclusions", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AgreementWorkTypeExclusion])
        IPostable.__init__(self, AgreementWorkTypeExclusion)
        IPaginateable.__init__(self, AgreementWorkTypeExclusion)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdWorktypeexclusionsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> FinanceAgreementsIdWorktypeexclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorktypeexclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorktypeexclusionsIdEndpoint: The initialized FinanceAgreementsIdWorktypeexclusionsIdEndpoint object.
        """
        child = FinanceAgreementsIdWorktypeexclusionsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AgreementWorkTypeExclusion]:
        """
        Performs a GET request against the /finance/agreements/{id}/workTypeExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkTypeExclusion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementWorkTypeExclusion,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AgreementWorkTypeExclusion]:
        """
        Performs a GET request against the /finance/agreements/{id}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkTypeExclusion]: The parsed response data.
        """
        return self._parse_many(
            AgreementWorkTypeExclusion,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AgreementWorkTypeExclusion:
        """
        Performs a POST request against the /finance/agreements/{id}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkTypeExclusion: The parsed response data.
        """
        return self._parse_one(
            AgreementWorkTypeExclusion,
            super()._make_request("POST", data=data, params=params).json(),
        )
