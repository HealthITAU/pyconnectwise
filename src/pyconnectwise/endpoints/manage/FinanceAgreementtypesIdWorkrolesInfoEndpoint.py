from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesInfoCountEndpoint import \
    FinanceAgreementtypesIdWorkrolesInfoCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesInfoIdEndpoint import \
    FinanceAgreementtypesIdWorkrolesInfoIdEndpoint
from pyconnectwise.models.manage import AgreementTypeWorkRoleInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdWorkrolesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesInfoCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdWorkrolesInfoIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorkrolesInfoIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorkrolesInfoIdEndpoint: The initialized FinanceAgreementtypesIdWorkrolesInfoIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorkrolesInfoIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AgreementTypeWorkRoleInfo]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRoleInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementTypeWorkRoleInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkRoleInfo]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRoleInfo]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeWorkRoleInfo, super()._make_request("GET", data=data, params=params).json()
        )
