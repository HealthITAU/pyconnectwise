from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdBoarddefaultsCountEndpoint import \
    FinanceAgreementtypesIdBoarddefaultsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdBoarddefaultsIdEndpoint import \
    FinanceAgreementtypesIdBoarddefaultsIdEndpoint
from pyconnectwise.models.manage import AgreementTypeBoardDefault
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdBoarddefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardDefaults", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdBoarddefaultsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdBoarddefaultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdBoarddefaultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdBoarddefaultsIdEndpoint: The initialized FinanceAgreementtypesIdBoarddefaultsIdEndpoint object.
        """
        child = FinanceAgreementtypesIdBoarddefaultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementTypeBoardDefault, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeBoardDefault]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeBoardDefault]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeBoardDefault, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeBoardDefault:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeBoardDefault: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeBoardDefault, super()._make_request("POST", data=data, params=params).json()
        )
