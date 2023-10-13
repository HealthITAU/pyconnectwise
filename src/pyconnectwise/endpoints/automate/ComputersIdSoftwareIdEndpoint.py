from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdSoftwareIdUninstallEndpoint import \
    ComputersIdSoftwareIdUninstallEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ComputersIdSoftwareIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.uninstall = self._register_child_endpoint(
            ComputersIdSoftwareIdUninstallEndpoint(client, parent_endpoint=self)
        )
