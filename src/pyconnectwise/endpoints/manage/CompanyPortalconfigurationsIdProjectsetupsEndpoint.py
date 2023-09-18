from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdProjectsetupsCountEndpoint import \
    CompanyPortalconfigurationsIdProjectsetupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdProjectsetupsIdEndpoint import \
    CompanyPortalconfigurationsIdProjectsetupsIdEndpoint
from pyconnectwise.models.manage import PortalConfigurationProjectSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsIdProjectsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectSetups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsIdProjectsetupsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalconfigurationsIdProjectsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdProjectsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdProjectsetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdProjectsetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdProjectsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationProjectSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/projectSetups endpoint and returns an initialized PaginatedResponse object.

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

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PortalConfigurationProjectSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/projectSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationProjectSetup]: The parsed response data.
        """
        return self._parse_many(
            PortalConfigurationProjectSetup, super()._make_request("GET", data=data, params=params).json()
        )
