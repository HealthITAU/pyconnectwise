from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdServicesetupsCountEndpoint import (
    CompanyPortalconfigurationsIdServicesetupsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdServicesetupsIdEndpoint import (
    CompanyPortalconfigurationsIdServicesetupsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import PortalConfigurationServiceSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyPortalconfigurationsIdServicesetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalConfigurationServiceSetup], ConnectWiseManageRequestParams],
    IPaginateable[PortalConfigurationServiceSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "serviceSetups", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PortalConfigurationServiceSetup])
        IPaginateable.__init__(self, PortalConfigurationServiceSetup)

        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsIdServicesetupsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> CompanyPortalconfigurationsIdServicesetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdServicesetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdServicesetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdServicesetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdServicesetupsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationServiceSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
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
            PortalConfigurationServiceSetup,
            super()._make_request("GET", data=data, params=params).json(),
        )
