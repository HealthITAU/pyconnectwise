from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyCountEndpoint import (
    CompanyM365contactsyncPropertyCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyExcludedEndpoint import (
    CompanyM365contactsyncPropertyExcludedEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyIncludedEndpoint import (
    CompanyM365contactsyncPropertyIncludedEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import M365ContactSyncProperty
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyM365contactsyncPropertyEndpoint(
    ConnectWiseEndpoint,
    IPostable[M365ContactSyncProperty, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "property", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, M365ContactSyncProperty)

        self.count = self._register_child_endpoint(
            CompanyM365contactsyncPropertyCountEndpoint(client, parent_endpoint=self)
        )
        self.excluded = self._register_child_endpoint(
            CompanyM365contactsyncPropertyExcludedEndpoint(client, parent_endpoint=self)
        )
        self.included = self._register_child_endpoint(
            CompanyM365contactsyncPropertyIncludedEndpoint(client, parent_endpoint=self)
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> M365ContactSyncProperty:
        """
        Performs a POST request against the /company/m365contactsync/property endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            M365ContactSyncProperty: The parsed response data.
        """
        return self._parse_one(
            M365ContactSyncProperty,
            super()._make_request("POST", data=data, params=params).json(),
        )
