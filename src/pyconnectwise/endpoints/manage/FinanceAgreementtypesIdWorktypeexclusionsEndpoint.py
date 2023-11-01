from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypeexclusionsCountEndpoint import (
    FinanceAgreementtypesIdWorktypeexclusionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint import (
    FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AgreementTypeWorkTypeExclusion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAgreementtypesIdWorktypeexclusionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementTypeWorkTypeExclusion], ConnectWiseManageRequestParams],
    IPostable[AgreementTypeWorkTypeExclusion, ConnectWiseManageRequestParams],
    IPaginateable[AgreementTypeWorkTypeExclusion, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "workTypeExclusions", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AgreementTypeWorkTypeExclusion])
        IPostable.__init__(self, AgreementTypeWorkTypeExclusion)
        IPaginateable.__init__(self, AgreementTypeWorkTypeExclusion)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypeexclusionsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint: The initialized FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AgreementTypeWorkTypeExclusion]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workTypeExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkTypeExclusion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementTypeWorkTypeExclusion,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AgreementTypeWorkTypeExclusion]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkTypeExclusion]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeWorkTypeExclusion,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AgreementTypeWorkTypeExclusion:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/workTypeExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkTypeExclusion: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeWorkTypeExclusion,
            super()._make_request("POST", data=data, params=params).json(),
        )
