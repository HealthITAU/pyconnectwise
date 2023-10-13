from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdAlertsuspensionsMaintenancewindowEndpoint import \
    ComputersIdAlertsuspensionsMaintenancewindowEndpoint
from pyconnectwise.endpoints.automate.ComputersIdAlertsuspensionsTemplatediversionEndpoint import \
    ComputersIdAlertsuspensionsTemplatediversionEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ComputersIdAlertsuspensionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Alertsuspensions", parent_endpoint=parent_endpoint)

        self.templatediversion = self._register_child_endpoint(
            ComputersIdAlertsuspensionsTemplatediversionEndpoint(client, parent_endpoint=self)
        )
        self.maintenancewindow = self._register_child_endpoint(
            ComputersIdAlertsuspensionsMaintenancewindowEndpoint(client, parent_endpoint=self)
        )
