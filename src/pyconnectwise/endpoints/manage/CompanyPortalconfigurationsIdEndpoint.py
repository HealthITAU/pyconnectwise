from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdInvoicesetupsEndpoint import (
    CompanyPortalconfigurationsIdInvoicesetupsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdOpportunitysetupsEndpoint import (
    CompanyPortalconfigurationsIdOpportunitysetupsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdPasswordemailsetupsEndpoint import (
    CompanyPortalconfigurationsIdPasswordemailsetupsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdProjectsetupsEndpoint import (
    CompanyPortalconfigurationsIdProjectsetupsEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdServicesetupsEndpoint import (
    CompanyPortalconfigurationsIdServicesetupsEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import PortalConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyPortalconfigurationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[PortalConfiguration, ConnectWiseManageRequestParams],
    IPatchable[PortalConfiguration, ConnectWiseManageRequestParams],
    IPuttable[PortalConfiguration, ConnectWiseManageRequestParams],
    IPaginateable[PortalConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, PortalConfiguration)
        IPatchable.__init__(self, PortalConfiguration)
        IPuttable.__init__(self, PortalConfiguration)
        IPaginateable.__init__(self, PortalConfiguration)

        self.invoice_setups = self._register_child_endpoint(
            CompanyPortalconfigurationsIdInvoicesetupsEndpoint(client, parent_endpoint=self)
        )
        self.service_setups = self._register_child_endpoint(
            CompanyPortalconfigurationsIdServicesetupsEndpoint(client, parent_endpoint=self)
        )
        self.project_setups = self._register_child_endpoint(
            CompanyPortalconfigurationsIdProjectsetupsEndpoint(client, parent_endpoint=self)
        )
        self.opportunity_setups = self._register_child_endpoint(
            CompanyPortalconfigurationsIdOpportunitysetupsEndpoint(client, parent_endpoint=self)
        )
        self.password_email_setups = self._register_child_endpoint(
            CompanyPortalconfigurationsIdPasswordemailsetupsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[PortalConfiguration]:
        """
        Performs a GET request against the /company/portalConfigurations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfiguration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalConfiguration, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> PortalConfiguration:
        """
        Performs a GET request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfiguration: The parsed response data.
        """
        return self._parse_one(PortalConfiguration, super()._make_request("GET", data=data, params=params).json())

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> PortalConfiguration:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfiguration: The parsed response data.
        """
        return self._parse_one(PortalConfiguration, super()._make_request("PATCH", data=data, params=params).json())

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> PortalConfiguration:
        """
        Performs a PUT request against the /company/portalConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfiguration: The parsed response data.
        """
        return self._parse_one(PortalConfiguration, super()._make_request("PUT", data=data, params=params).json())
