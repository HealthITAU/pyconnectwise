from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint import \
    CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint
from pyconnectwise.models.manage import PortalConfigurationPasswordEmailSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsIdPasswordemailsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "passwordEmailSetups", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationPasswordEmailSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/passwordEmailSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationPasswordEmailSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationPasswordEmailSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PortalConfigurationPasswordEmailSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/passwordEmailSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationPasswordEmailSetup]: The parsed response data.
        """
        return self._parse_many(
            PortalConfigurationPasswordEmailSetup, super()._make_request("GET", data=data, params=params).json()
        )
