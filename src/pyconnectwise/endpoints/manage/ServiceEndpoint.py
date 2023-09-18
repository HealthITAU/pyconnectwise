from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsEndpoint import ServiceBoardsEndpoint
from pyconnectwise.endpoints.manage.ServiceCodesEndpoint import ServiceCodesEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailtemplatesEndpoint import ServiceEmailtemplatesEndpoint
from pyconnectwise.endpoints.manage.ServiceImpactsEndpoint import ServiceImpactsEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoEndpoint import ServiceInfoEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasearticlesEndpoint import ServiceKnowledgebasearticlesEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasecategoriesEndpoint import ServiceKnowledgebasecategoriesEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesettingsEndpoint import ServiceKnowledgebasesettingsEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesubcategoriesEndpoint import \
    ServiceKnowledgebasesubcategoriesEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsEndpoint import ServiceLocationsEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesEndpoint import ServicePrioritiesEndpoint
from pyconnectwise.endpoints.manage.ServicePriorityEndpoint import ServicePriorityEndpoint
from pyconnectwise.endpoints.manage.ServiceSchedulingEndpoint import ServiceSchedulingEndpoint
from pyconnectwise.endpoints.manage.ServiceServicesignoffEndpoint import ServiceServicesignoffEndpoint
from pyconnectwise.endpoints.manage.ServiceSeveritiesEndpoint import ServiceSeveritiesEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasEndpoint import ServiceSlasEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesEndpoint import ServiceSourcesEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysEndpoint import ServiceSurveysEndpoint
from pyconnectwise.endpoints.manage.ServiceTeammembersEndpoint import ServiceTeammembersEndpoint
from pyconnectwise.endpoints.manage.ServiceTeamsEndpoint import ServiceTeamsEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesEndpoint import ServiceTemplatesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksEndpoint import ServiceTicketlinksEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsEndpoint import ServiceTicketsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsyncsEndpoint import ServiceTicketsyncsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "service", parent_endpoint=parent_endpoint)

        self.s_l_as = self._register_child_endpoint(ServiceSlasEndpoint(client, parent_endpoint=self))
        self.slas = self._register_child_endpoint(ServiceSlasEndpoint(client, parent_endpoint=self))
        self.scheduling = self._register_child_endpoint(ServiceSchedulingEndpoint(client, parent_endpoint=self))
        self.sources = self._register_child_endpoint(ServiceSourcesEndpoint(client, parent_endpoint=self))
        self.codes = self._register_child_endpoint(ServiceCodesEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceInfoEndpoint(client, parent_endpoint=self))
        self.surveys = self._register_child_endpoint(ServiceSurveysEndpoint(client, parent_endpoint=self))
        self.teams = self._register_child_endpoint(ServiceTeamsEndpoint(client, parent_endpoint=self))
        self.service_signoff = self._register_child_endpoint(
            ServiceServicesignoffEndpoint(client, parent_endpoint=self)
        )
        self.knowledge_base_categories = self._register_child_endpoint(
            ServiceKnowledgebasecategoriesEndpoint(client, parent_endpoint=self)
        )
        self.tickets = self._register_child_endpoint(ServiceTicketsEndpoint(client, parent_endpoint=self))
        self.priority = self._register_child_endpoint(ServicePriorityEndpoint(client, parent_endpoint=self))
        self.ticket_links = self._register_child_endpoint(ServiceTicketlinksEndpoint(client, parent_endpoint=self))
        self.knowledge_base_sub_categories = self._register_child_endpoint(
            ServiceKnowledgebasesubcategoriesEndpoint(client, parent_endpoint=self)
        )
        self.knowledge_base_articles = self._register_child_endpoint(
            ServiceKnowledgebasearticlesEndpoint(client, parent_endpoint=self)
        )
        self.ticket_syncs = self._register_child_endpoint(ServiceTicketsyncsEndpoint(client, parent_endpoint=self))
        self.email_templates = self._register_child_endpoint(
            ServiceEmailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.impacts = self._register_child_endpoint(ServiceImpactsEndpoint(client, parent_endpoint=self))
        self.templates = self._register_child_endpoint(ServiceTemplatesEndpoint(client, parent_endpoint=self))
        self.team_members = self._register_child_endpoint(ServiceTeammembersEndpoint(client, parent_endpoint=self))
        self.priorities = self._register_child_endpoint(ServicePrioritiesEndpoint(client, parent_endpoint=self))
        self.severities = self._register_child_endpoint(ServiceSeveritiesEndpoint(client, parent_endpoint=self))
        self.knowledgebasesettings = self._register_child_endpoint(
            ServiceKnowledgebasesettingsEndpoint(client, parent_endpoint=self)
        )
        self.locations = self._register_child_endpoint(ServiceLocationsEndpoint(client, parent_endpoint=self))
        self.boards = self._register_child_endpoint(ServiceBoardsEndpoint(client, parent_endpoint=self))
