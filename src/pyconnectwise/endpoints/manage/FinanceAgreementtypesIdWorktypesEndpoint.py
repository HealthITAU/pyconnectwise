from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypesCountEndpoint import \
    FinanceAgreementtypesIdWorktypesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypesIdEndpoint import \
    FinanceAgreementtypesIdWorktypesIdEndpoint
from pyconnectwise.models.manage import AgreementTypeWorkType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdWorktypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "worktypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdWorktypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorktypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorktypesIdEndpoint: The initialized FinanceAgreementtypesIdWorktypesIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorktypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementTypeWorkType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkType]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkType]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkType:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/worktypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkType: The parsed response data.
        """
        return self._parse_one(AgreementTypeWorkType, super()._make_request("POST", data=data, params=params).json())
