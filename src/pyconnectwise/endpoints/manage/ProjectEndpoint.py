from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBillingratesEndpoint import ProjectBillingratesEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsEndpoint import ProjectBoardsEndpoint
from pyconnectwise.endpoints.manage.ProjectIdEndpoint import ProjectIdEndpoint
from pyconnectwise.endpoints.manage.ProjectPhasestatusesEndpoint import ProjectPhasestatusesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsEndpoint import ProjectProjectsEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesEndpoint import ProjectProjecttemplatesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttypesEndpoint import ProjectProjecttypesEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityrolesEndpoint import ProjectSecurityrolesEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesEndpoint import ProjectStatusesEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusindicatorsEndpoint import ProjectStatusindicatorsEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketnoteEndpoint import ProjectTicketnoteEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsEndpoint import ProjectTicketsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "project", parent_endpoint=parent_endpoint)

        self.phase_statuses = self._register_child_endpoint(ProjectPhasestatusesEndpoint(client, parent_endpoint=self))
        self.ticket_note = self._register_child_endpoint(ProjectTicketnoteEndpoint(client, parent_endpoint=self))
        self.project_types = self._register_child_endpoint(ProjectProjecttypesEndpoint(client, parent_endpoint=self))
        self.boards = self._register_child_endpoint(ProjectBoardsEndpoint(client, parent_endpoint=self))
        self.projects = self._register_child_endpoint(ProjectProjectsEndpoint(client, parent_endpoint=self))
        self.billing_rates = self._register_child_endpoint(ProjectBillingratesEndpoint(client, parent_endpoint=self))
        self.tickets = self._register_child_endpoint(ProjectTicketsEndpoint(client, parent_endpoint=self))
        self.project_templates = self._register_child_endpoint(
            ProjectProjecttemplatesEndpoint(client, parent_endpoint=self)
        )
        self.security_roles = self._register_child_endpoint(ProjectSecurityrolesEndpoint(client, parent_endpoint=self))
        self.status_indicators = self._register_child_endpoint(
            ProjectStatusindicatorsEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self._register_child_endpoint(ProjectStatusesEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectIdEndpoint: The initialized ProjectIdEndpoint object.
        """
        child = ProjectIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
