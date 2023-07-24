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
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import ManagedDevicesIntegration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManageddevicesintegrationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.notifications = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.cross_references = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdCrossreferencesEndpoint(client, parent_endpoint=self)
        )
        self.logins = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdLoginsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDevicesIntegration,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegration:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegration, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super()._make_request("DELETE", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegration:
        """
        Performs a PUT request against the /company/managedDevicesIntegrations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegration, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegration:
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
