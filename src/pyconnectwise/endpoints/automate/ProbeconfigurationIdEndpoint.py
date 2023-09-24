from typing import Any

from pyconnectwise.endpoints.automate.ProbeconfigurationIdAgentpushcredentialsEndpoint import \
    ProbeconfigurationIdAgentpushcredentialsEndpoint
from pyconnectwise.endpoints.automate.ProbeconfigurationIdSnmpconfigurationEndpoint import \
    ProbeconfigurationIdSnmpconfigurationEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProbeconfigurationIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.agentpushcredentials = self._register_child_endpoint(
            ProbeconfigurationIdAgentpushcredentialsEndpoint(client, parent_endpoint=self)
        )
        self.snmpconfiguration = self._register_child_endpoint(
            ProbeconfigurationIdSnmpconfigurationEndpoint(client, parent_endpoint=self)
        )
