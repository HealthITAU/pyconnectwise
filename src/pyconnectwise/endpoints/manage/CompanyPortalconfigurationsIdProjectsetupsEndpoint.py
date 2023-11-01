from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdProjectsetupsCountEndpoint import (
    CompanyPortalconfigurationsIdProjectsetupsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdProjectsetupsIdEndpoint import (
    CompanyPortalconfigurationsIdProjectsetupsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import PortalConfigurationProjectSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyPortalconfigurationsIdProjectsetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalConfigurationProjectSetup], ConnectWiseManageRequestParams],
    IPaginateable[PortalConfigurationProjectSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "projectSetups", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PortalConfigurationProjectSetup])
        IPaginateable.__init__(self, PortalConfigurationProjectSetup)

        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsIdProjectsetupsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(
        self, id: int  # noqa: A002
    ) -> CompanyPortalconfigurationsIdProjectsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdProjectsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdProjectsetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdProjectsetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdProjectsetupsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationProjectSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
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
            PortalConfigurationProjectSetup,
            super()._make_request("GET", data=data, params=params).json(),
        )
