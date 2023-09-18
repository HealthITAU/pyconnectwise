from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesCountEndpoint import \
    FinanceAgreementtypesIdWorkrolesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesIdEndpoint import \
    FinanceAgreementtypesIdWorkrolesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesInfoEndpoint import \
    FinanceAgreementtypesIdWorkrolesInfoEndpoint
from pyconnectwise.models.manage import AgreementTypeWorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdWorkrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workroles", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdWorkrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorkrolesIdEndpoint: The initialized FinanceAgreementtypesIdWorkrolesIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementTypeWorkRole, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkRole]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRole]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkRole, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkRole:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkRole: The parsed response data.
        """
        return self._parse_one(AgreementTypeWorkRole, super()._make_request("POST", data=data, params=params).json())
