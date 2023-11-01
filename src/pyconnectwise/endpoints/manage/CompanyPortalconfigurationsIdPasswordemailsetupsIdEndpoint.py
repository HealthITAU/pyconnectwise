from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import PortalConfigurationPasswordEmailSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyPortalconfigurationsIdPasswordemailsetupsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[PortalConfigurationPasswordEmailSetup, ConnectWiseManageRequestParams],
    IPuttable[PortalConfigurationPasswordEmailSetup, ConnectWiseManageRequestParams],
    IPatchable[PortalConfigurationPasswordEmailSetup, ConnectWiseManageRequestParams],
    IPaginateable[
        PortalConfigurationPasswordEmailSetup, ConnectWiseManageRequestParams
    ],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, PortalConfigurationPasswordEmailSetup)
        IPuttable.__init__(self, PortalConfigurationPasswordEmailSetup)
        IPatchable.__init__(self, PortalConfigurationPasswordEmailSetup)
        IPaginateable.__init__(self, PortalConfigurationPasswordEmailSetup)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PortalConfigurationPasswordEmailSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/passwordEmailSetups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationPasswordEmailSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationPasswordEmailSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationPasswordEmailSetup:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/passwordEmailSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationPasswordEmailSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationPasswordEmailSetup,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationPasswordEmailSetup:
        """
        Performs a PUT request against the /company/portalConfigurations/{id}/passwordEmailSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationPasswordEmailSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationPasswordEmailSetup,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationPasswordEmailSetup:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id}/passwordEmailSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationPasswordEmailSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationPasswordEmailSetup,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
