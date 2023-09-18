from typing import Any

from pyconnectwise.endpoints.automate.PatchactionsDeployallapprovedEndpoint import PatchactionsDeployallapprovedEndpoint
from pyconnectwise.endpoints.automate.PatchactionsDeployallsecurityEndpoint import PatchactionsDeployallsecurityEndpoint
from pyconnectwise.endpoints.automate.PatchactionsReattemptfailedEndpoint import PatchactionsReattemptfailedEndpoint
from pyconnectwise.endpoints.automate.PatchactionsSettopilotstageEndpoint import PatchactionsSettopilotstageEndpoint
from pyconnectwise.endpoints.automate.PatchactionsSettoproductionstageEndpoint import \
    PatchactionsSettoproductionstageEndpoint
from pyconnectwise.endpoints.automate.PatchactionsSettoteststageEndpoint import PatchactionsSettoteststageEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class PatchactionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Patchactions", parent_endpoint=parent_endpoint)

        self.settoteststage = self._register_child_endpoint(
            PatchactionsSettoteststageEndpoint(client, parent_endpoint=self)
        )
        self.settopilotstage = self._register_child_endpoint(
            PatchactionsSettopilotstageEndpoint(client, parent_endpoint=self)
        )
        self.reattemptfailed = self._register_child_endpoint(
            PatchactionsReattemptfailedEndpoint(client, parent_endpoint=self)
        )
        self.deployallapproved = self._register_child_endpoint(
            PatchactionsDeployallapprovedEndpoint(client, parent_endpoint=self)
        )
        self.settoproductionstage = self._register_child_endpoint(
            PatchactionsSettoproductionstageEndpoint(client, parent_endpoint=self)
        )
        self.deployallsecurity = self._register_child_endpoint(
            PatchactionsDeployallsecurityEndpoint(client, parent_endpoint=self)
        )
