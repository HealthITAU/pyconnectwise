from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectPhaseStatusesEndpoint import ProjectPhaseStatusesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsEndpoint import ProjectProjectsEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectTypesEndpoint import ProjectProjectTypesEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityRolesEndpoint import ProjectSecurityRolesEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesEndpoint import ProjectStatusesEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusIndicatorsEndpoint import ProjectStatusIndicatorsEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsEndpoint import ProjectTicketsEndpoint

class ProjectEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "project")
        
        self.phaseStatuses = self.register_child_endpoint(
            ProjectPhaseStatusesEndpoint(client, parent_endpoint=self)
        )
        self.projects = self.register_child_endpoint(
            ProjectProjectsEndpoint(client, parent_endpoint=self)
        )
        self.projectTypes = self.register_child_endpoint(
            ProjectProjectTypesEndpoint(client, parent_endpoint=self)
        )
        self.securityRoles = self.register_child_endpoint(
            ProjectSecurityRolesEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            ProjectStatusesEndpoint(client, parent_endpoint=self)
        )
        self.statusIndicators = self.register_child_endpoint(
            ProjectStatusIndicatorsEndpoint(client, parent_endpoint=self)
        )
        self.tickets = self.register_child_endpoint(
            ProjectTicketsEndpoint(client, parent_endpoint=self)
        )