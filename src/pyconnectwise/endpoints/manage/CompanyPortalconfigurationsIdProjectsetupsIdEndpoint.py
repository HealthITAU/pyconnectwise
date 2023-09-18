from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import PortalConfigurationProjectSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsIdProjectsetupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationProjectSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/projectSetups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationProjectSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalConfigurationProjectSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationProjectSetup:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/projectSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationProjectSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationProjectSetup, super()._make_request("GET", data=data, params=params).json()
        )

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationProjectSetup:
        """
        Performs a PUT request against the /company/portalConfigurations/{id}/projectSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationProjectSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationProjectSetup, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationProjectSetup:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id}/projectSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationProjectSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationProjectSetup, super()._make_request("PATCH", data=data, params=params).json()
        )
