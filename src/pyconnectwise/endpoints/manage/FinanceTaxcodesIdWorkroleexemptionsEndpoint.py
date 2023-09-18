from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsCountEndpoint import \
    FinanceTaxcodesIdWorkroleexemptionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdWorkroleexemptionsIdEndpoint import \
    FinanceTaxcodesIdWorkroleexemptionsIdEndpoint
from pyconnectwise.models.manage import WorkRoleExemption
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceTaxcodesIdWorkroleexemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExemptions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdWorkroleexemptionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdWorkroleexemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdWorkroleexemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdWorkroleexemptionsIdEndpoint: The initialized FinanceTaxcodesIdWorkroleexemptionsIdEndpoint object.
        """
        child = FinanceTaxcodesIdWorkroleexemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[WorkRoleExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRoleExemption]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkRoleExemption, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkRoleExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/workRoleExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRoleExemption]: The parsed response data.
        """
        return self._parse_many(WorkRoleExemption, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleExemption:
        """
        Performs a POST request against the /finance/taxCodes/{id}/workRoleExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleExemption: The parsed response data.
        """
        return self._parse_one(WorkRoleExemption, super()._make_request("POST", data=data, params=params).json())
