from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkroleexclusionsCountEndpoint import \
    FinanceAgreementtypesIdWorkroleexclusionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint import \
    FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint
from pyconnectwise.models.manage import AgreementTypeWorkRoleExclusion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdWorkroleexclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExclusions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkroleexclusionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint: The initialized FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint object.
        """
        child = FinanceAgreementtypesIdWorkroleexclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AgreementTypeWorkRoleExclusion]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workRoleExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRoleExclusion]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementTypeWorkRoleExclusion, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkRoleExclusion]:
        """
        Performs a GET request against the /finance/agreementTypes/{id}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRoleExclusion]: The parsed response data.
        """
        return self._parse_many(
            AgreementTypeWorkRoleExclusion, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkRoleExclusion:
        """
        Performs a POST request against the /finance/agreementTypes/{id}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkRoleExclusion: The parsed response data.
        """
        return self._parse_one(
            AgreementTypeWorkRoleExclusion, super()._make_request("POST", data=data, params=params).json()
        )
