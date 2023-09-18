from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyOwnershiptypesCountEndpoint import CompanyOwnershiptypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyOwnershiptypesIdEndpoint import CompanyOwnershiptypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyOwnershiptypesInfoEndpoint import CompanyOwnershiptypesInfoEndpoint
from pyconnectwise.models.manage import OwnershipType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyOwnershiptypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ownershipTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyOwnershiptypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyOwnershiptypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyOwnershiptypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyOwnershiptypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyOwnershiptypesIdEndpoint: The initialized CompanyOwnershiptypesIdEndpoint object.
        """
        child = CompanyOwnershiptypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OwnershipType]:
        """
        Performs a GET request against the /company/ownershipTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OwnershipType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OwnershipType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OwnershipType]:
        """
        Performs a GET request against the /company/ownershipTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OwnershipType]: The parsed response data.
        """
        return self._parse_many(OwnershipType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OwnershipType:
        """
        Performs a POST request against the /company/ownershipTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OwnershipType: The parsed response data.
        """
        return self._parse_one(OwnershipType, super()._make_request("POST", data=data, params=params).json())
