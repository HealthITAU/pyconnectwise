from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdInvoicesetupsIdTesttransactionEndpoint import (
    CompanyPortalconfigurationsIdInvoicesetupsIdTesttransactionEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import PortalConfigurationInvoiceSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[PortalConfigurationInvoiceSetup, ConnectWiseManageRequestParams],
    IPuttable[PortalConfigurationInvoiceSetup, ConnectWiseManageRequestParams],
    IPatchable[PortalConfigurationInvoiceSetup, ConnectWiseManageRequestParams],
    IPaginateable[PortalConfigurationInvoiceSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, PortalConfigurationInvoiceSetup)
        IPuttable.__init__(self, PortalConfigurationInvoiceSetup)
        IPatchable.__init__(self, PortalConfigurationInvoiceSetup)
        IPaginateable.__init__(self, PortalConfigurationInvoiceSetup)

        self.test_transaction = self._register_child_endpoint(
            CompanyPortalconfigurationsIdInvoicesetupsIdTesttransactionEndpoint(
                client, parent_endpoint=self
            )
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PortalConfigurationInvoiceSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationInvoiceSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationInvoiceSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationInvoiceSetup:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationInvoiceSetup,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationInvoiceSetup:
        """
        Performs a PUT request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationInvoiceSetup,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalConfigurationInvoiceSetup:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationInvoiceSetup,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
