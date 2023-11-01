from typing import Any

from pyconnectwise.endpoints.automate.LookupsProbeeventlevelsEndpoint import (
    LookupsProbeeventlevelsEndpoint,
)
from pyconnectwise.endpoints.automate.LookupsScanfrequenciesEndpoint import (
    LookupsScanfrequenciesEndpoint,
)
from pyconnectwise.endpoints.automate.LookupsSnmpencryptionmethodsEndpoint import (
    LookupsSnmpencryptionmethodsEndpoint,
)
from pyconnectwise.endpoints.automate.LookupsSnmphashmethodsEndpoint import (
    LookupsSnmphashmethodsEndpoint,
)
from pyconnectwise.endpoints.automate.LookupsStatusscannetworkportoptionsEndpoint import (
    LookupsStatusscannetworkportoptionsEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class LookupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Lookups", parent_endpoint=parent_endpoint
        )

        self.probeeventlevels = self._register_child_endpoint(
            LookupsProbeeventlevelsEndpoint(client, parent_endpoint=self)
        )
        self.snmphashmethods = self._register_child_endpoint(
            LookupsSnmphashmethodsEndpoint(client, parent_endpoint=self)
        )
        self.snmpencryptionmethods = self._register_child_endpoint(
            LookupsSnmpencryptionmethodsEndpoint(client, parent_endpoint=self)
        )
        self.scanfrequencies = self._register_child_endpoint(
            LookupsScanfrequenciesEndpoint(client, parent_endpoint=self)
        )
        self.statusscannetworkportoptions = self._register_child_endpoint(
            LookupsStatusscannetworkportoptionsEndpoint(client, parent_endpoint=self)
        )
