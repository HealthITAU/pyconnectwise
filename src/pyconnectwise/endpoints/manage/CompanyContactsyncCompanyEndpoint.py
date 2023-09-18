from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsyncCompanyCountEndpoint import CompanyContactsyncCompanyCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsyncCompanyIdEndpoint import CompanyContactsyncCompanyIdEndpoint
from pyconnectwise.models.manage import M365ContactSyncCompany
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsyncCompanyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "company", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyContactsyncCompanyCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyContactsyncCompanyIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsyncCompanyIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsyncCompanyIdEndpoint: The initialized CompanyContactsyncCompanyIdEndpoint object.
        """
        child = CompanyContactsyncCompanyIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[M365ContactSyncCompany]:
        """
        Performs a GET request against the /company/contactsync/company endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[M365ContactSyncCompany]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), M365ContactSyncCompany, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[M365ContactSyncCompany]:
        """
        Performs a GET request against the /company/contactsync/company endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[M365ContactSyncCompany]: The parsed response data.
        """
        return self._parse_many(M365ContactSyncCompany, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /company/contactsync/company endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
