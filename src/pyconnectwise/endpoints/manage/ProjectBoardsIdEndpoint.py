from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsEndpoint import (
    ProjectBoardsIdTeamsEndpoint,
)


class ProjectBoardsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.teams = self._register_child_endpoint(
            ProjectBoardsIdTeamsEndpoint(client, parent_endpoint=self)
        )
