from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalsecuritysettingsCountEndpoint import \
    CompanyPortalsecuritysettingsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalsecuritysettingsIdEndpoint import \
    CompanyPortalsecuritysettingsIdEndpoint
from pyconnectwise.models.manage import PortalSecuritySetting
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalsecuritysettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalSecuritySettings", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyPortalsecuritysettingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalsecuritysettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalsecuritysettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalsecuritysettingsIdEndpoint: The initialized CompanyPortalsecuritysettingsIdEndpoint object.
        """
        child = CompanyPortalsecuritysettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalSecuritySetting]:
        """
        Performs a GET request against the /company/portalSecuritySettings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalSecuritySetting]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalSecuritySetting, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalSecuritySetting]:
        """
        Performs a GET request against the /company/portalSecuritySettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalSecuritySetting]: The parsed response data.
        """
        return self._parse_many(PortalSecuritySetting, super()._make_request("GET", data=data, params=params).json())
