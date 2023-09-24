from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdCrossreferencesEndpoint import \
    CompanyManageddevicesintegrationsIdCrossreferencesEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdInfoEndpoint import \
    CompanyManageddevicesintegrationsIdInfoEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdLoginsEndpoint import \
    CompanyManageddevicesintegrationsIdLoginsEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdNotificationsEndpoint import \
    CompanyManageddevicesintegrationsIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdUsagesEndpoint import \
    CompanyManageddevicesintegrationsIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ManagedDevicesIntegration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyManageddevicesintegrationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ManagedDevicesIntegration, ConnectWiseManageRequestParams],
    IPuttable[ManagedDevicesIntegration, ConnectWiseManageRequestParams],
    IPatchable[ManagedDevicesIntegration, ConnectWiseManageRequestParams],
    IPaginateable[ManagedDevicesIntegration, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.notifications = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.logins = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdLoginsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.cross_references = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdCrossreferencesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ManagedDevicesIntegration]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagedDevicesIntegration, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegration:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegration, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegration:
        """
        Performs a PUT request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegration, super()._make_request("PUT", data=data, params=params).json())

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegration:
        """
        Performs a PATCH request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegration, super()._make_request("PATCH", data=data, params=params).json()
        )
