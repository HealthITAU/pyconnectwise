from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsEndpoint import ProjectBoardsEndpoint
from pyconnectwise.endpoints.manage.ProjectPhasestatusesEndpoint import ProjectPhasestatusesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsEndpoint import ProjectProjectsEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttypesEndpoint import ProjectProjecttypesEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityrolesEndpoint import ProjectSecurityrolesEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesEndpoint import ProjectStatusesEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusindicatorsEndpoint import ProjectStatusindicatorsEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketnoteEndpoint import ProjectTicketnoteEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsEndpoint import ProjectTicketsEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProjectEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "project", parent_endpoint=parent_endpoint)

        self.boards = self._register_child_endpoint(ProjectBoardsEndpoint(client, parent_endpoint=self))
        self.phase_statuses = self._register_child_endpoint(ProjectPhasestatusesEndpoint(client, parent_endpoint=self))
        self.project_types = self._register_child_endpoint(ProjectProjecttypesEndpoint(client, parent_endpoint=self))
        self.projects = self._register_child_endpoint(ProjectProjectsEndpoint(client, parent_endpoint=self))
        self.security_roles = self._register_child_endpoint(ProjectSecurityrolesEndpoint(client, parent_endpoint=self))
        self.status_indicators = self._register_child_endpoint(
            ProjectStatusindicatorsEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self._register_child_endpoint(ProjectStatusesEndpoint(client, parent_endpoint=self))
        self.ticket_note = self._register_child_endpoint(ProjectTicketnoteEndpoint(client, parent_endpoint=self))
        self.tickets = self._register_child_endpoint(ProjectTicketsEndpoint(client, parent_endpoint=self))
