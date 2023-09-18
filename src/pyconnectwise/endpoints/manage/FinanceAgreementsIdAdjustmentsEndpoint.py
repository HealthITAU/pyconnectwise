from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdjustmentsCountEndpoint import \
    FinanceAgreementsIdAdjustmentsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdjustmentsIdEndpoint import \
    FinanceAgreementsIdAdjustmentsIdEndpoint
from pyconnectwise.models.manage import AgreementAdjustment
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsIdAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdAdjustmentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdAdjustmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdAdjustmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdAdjustmentsIdEndpoint: The initialized FinanceAgreementsIdAdjustmentsIdEndpoint object.
        """
        child = FinanceAgreementsIdAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AgreementAdjustment]:
        """
        Performs a GET request against the /finance/agreements/{id}/adjustments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementAdjustment]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementAdjustment, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementAdjustment]:
        """
        Performs a GET request against the /finance/agreements/{id}/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementAdjustment]: The parsed response data.
        """
        return self._parse_many(AgreementAdjustment, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementAdjustment:
        """
        Performs a POST request against the /finance/agreements/{id}/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementAdjustment: The parsed response data.
        """
        return self._parse_one(AgreementAdjustment, super()._make_request("POST", data=data, params=params).json())
