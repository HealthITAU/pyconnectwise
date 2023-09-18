from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyCountEndpoint import \
    CompanyM365contactsyncPropertyCountEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyExcludedEndpoint import \
    CompanyM365contactsyncPropertyExcludedEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyIncludedEndpoint import \
    CompanyM365contactsyncPropertyIncludedEndpoint
from pyconnectwise.models.manage import M365ContactSyncProperty
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyM365contactsyncPropertyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "property", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyM365contactsyncPropertyCountEndpoint(client, parent_endpoint=self)
        )
        self.excluded = self._register_child_endpoint(
            CompanyM365contactsyncPropertyExcludedEndpoint(client, parent_endpoint=self)
        )
        self.included = self._register_child_endpoint(
            CompanyM365contactsyncPropertyIncludedEndpoint(client, parent_endpoint=self)
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> M365ContactSyncProperty:
        """
        Performs a POST request against the /company/m365contactsync/property endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            M365ContactSyncProperty: The parsed response data.
        """
        return self._parse_one(M365ContactSyncProperty, super()._make_request("POST", data=data, params=params).json())
