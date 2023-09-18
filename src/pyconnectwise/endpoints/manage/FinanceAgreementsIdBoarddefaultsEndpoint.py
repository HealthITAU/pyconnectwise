from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoarddefaultsCountEndpoint import \
    FinanceAgreementsIdBoarddefaultsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoarddefaultsIdEndpoint import \
    FinanceAgreementsIdBoarddefaultsIdEndpoint
from pyconnectwise.models.manage import BoardDefault
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsIdBoarddefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardDefaults", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdBoarddefaultsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdBoarddefaultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdBoarddefaultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdBoarddefaultsIdEndpoint: The initialized FinanceAgreementsIdBoarddefaultsIdEndpoint object.
        """
        child = FinanceAgreementsIdBoarddefaultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[BoardDefault]:
        """
        Performs a GET request against the /finance/agreements/{id}/boardDefaults endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardDefault]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardDefault, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardDefault]:
        """
        Performs a GET request against the /finance/agreements/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardDefault]: The parsed response data.
        """
        return self._parse_many(BoardDefault, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardDefault:
        """
        Performs a POST request against the /finance/agreements/{id}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardDefault: The parsed response data.
        """
        return self._parse_one(BoardDefault, super()._make_request("POST", data=data, params=params).json())
