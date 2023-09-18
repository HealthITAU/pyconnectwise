from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import AgreementTypeWorkTypeExclusion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdWorktypeexclusionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AgreementTypeWorkTypeExclusion]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workTypeExclusions/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkTypeExclusion]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementTypeWorkTypeExclusion, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkTypeExclusion:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workTypeExclusions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkTypeExclusion: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeWorkTypeExclusion, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /finance/agreementTypes/{id}/workTypeExclusions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
