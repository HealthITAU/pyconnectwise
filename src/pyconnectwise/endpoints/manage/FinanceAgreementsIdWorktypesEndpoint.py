from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypesCountEndpoint import \
    FinanceAgreementsIdWorktypesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypesIdEndpoint import FinanceAgreementsIdWorktypesIdEndpoint
from pyconnectwise.models.manage import AgreementWorkType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsIdWorktypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "worktypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdWorktypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdWorktypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdWorktypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdWorktypesIdEndpoint: The initialized FinanceAgreementsIdWorktypesIdEndpoint object.
        """
        child = FinanceAgreementsIdWorktypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AgreementWorkType]:
        """
        Performs a GET request against the /finance/agreements/{id}/worktypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementWorkType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementWorkType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementWorkType]:
        """
        Performs a GET request against the /finance/agreements/{id}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementWorkType]: The parsed response data.
        """
        return self._parse_many(AgreementWorkType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementWorkType:
        """
        Performs a POST request against the /finance/agreements/{id}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementWorkType: The parsed response data.
        """
        return self._parse_one(AgreementWorkType, super()._make_request("POST", data=data, params=params).json())
