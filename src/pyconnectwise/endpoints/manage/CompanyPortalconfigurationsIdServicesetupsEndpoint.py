from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdServicesetupsCountEndpoint import \
    CompanyPortalconfigurationsIdServicesetupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdServicesetupsIdEndpoint import \
    CompanyPortalconfigurationsIdServicesetupsIdEndpoint
from pyconnectwise.models.manage import PortalConfigurationServiceSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsIdServicesetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "serviceSetups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsIdServicesetupsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalconfigurationsIdServicesetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdServicesetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdServicesetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdServicesetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdServicesetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationServiceSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/serviceSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationServiceSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalConfigurationServiceSetup, self, page, page_size, params
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PortalConfigurationServiceSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/serviceSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationServiceSetup]: The parsed response data.
        """
        return self._parse_many(
            PortalConfigurationServiceSetup, super()._make_request("GET", data=data, params=params).json()
        )
