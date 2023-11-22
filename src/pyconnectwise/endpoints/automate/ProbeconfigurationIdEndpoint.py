from pyconnectwise.endpoints.automate.ProbeconfigurationIdAgentpushcredentialsEndpoint import (
    ProbeconfigurationIdAgentpushcredentialsEndpoint,
)
from pyconnectwise.endpoints.automate.ProbeconfigurationIdSnmpconfigurationEndpoint import (
    ProbeconfigurationIdSnmpconfigurationEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ProbeconfigurationIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.agentpushcredentials = self._register_child_endpoint(
            ProbeconfigurationIdAgentpushcredentialsEndpoint(client, parent_endpoint=self)
        )
        self.snmpconfiguration = self._register_child_endpoint(
            ProbeconfigurationIdSnmpconfigurationEndpoint(client, parent_endpoint=self)
        )
