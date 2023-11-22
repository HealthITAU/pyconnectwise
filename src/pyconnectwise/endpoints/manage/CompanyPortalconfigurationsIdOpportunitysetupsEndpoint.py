from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint import (
    CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import PortalConfigurationOpportunitySetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyPortalconfigurationsIdOpportunitysetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalConfigurationOpportunitySetup], ConnectWiseManageRequestParams],
    IPatchable[PortalConfigurationOpportunitySetup, ConnectWiseManageRequestParams],
    IPuttable[PortalConfigurationOpportunitySetup, ConnectWiseManageRequestParams],
    IPaginateable[PortalConfigurationOpportunitySetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "opportunitySetups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[PortalConfigurationOpportunitySetup])
        IPatchable.__init__(self, PortalConfigurationOpportunitySetup)
        IPuttable.__init__(self, PortalConfigurationOpportunitySetup)
        IPaginateable.__init__(self, PortalConfigurationOpportunitySetup)

    def id(self, _id: int) -> CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdOpportunitysetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[PortalConfigurationOpportunitySetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/opportunitySetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationOpportunitySetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationOpportunitySetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[PortalConfigurationOpportunitySetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/opportunitySetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationOpportunitySetup]: The parsed response data.
        """
        return self._parse_many(
            PortalConfigurationOpportunitySetup, super()._make_request("GET", data=data, params=params).json()
        )

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> PortalConfigurationOpportunitySetup:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id}/opportunitySetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationOpportunitySetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationOpportunitySetup, super()._make_request("PATCH", data=data, params=params).json()
        )

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> PortalConfigurationOpportunitySetup:
        """
        Performs a PUT request against the /company/portalConfigurations/{id}/opportunitySetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationOpportunitySetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationOpportunitySetup, super()._make_request("PUT", data=data, params=params).json()
        )
