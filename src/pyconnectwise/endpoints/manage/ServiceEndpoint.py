from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsEndpoint import ServiceBoardsEndpoint
from pyconnectwise.endpoints.manage.ServiceCodesEndpoint import ServiceCodesEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailTemplatesEndpoint import ServiceEmailTemplatesEndpoint
from pyconnectwise.endpoints.manage.ServiceImpactsEndpoint import ServiceImpactsEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseArticlesEndpoint import ServiceKnowledgeBaseArticlesEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseCategoriesEndpoint import ServiceKnowledgeBaseCategoriesEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesettingsEndpoint import ServiceKnowledgebasesettingsEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseSubCategoriesEndpoint import ServiceKnowledgeBaseSubCategoriesEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsEndpoint import ServiceLocationsEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesEndpoint import ServicePrioritiesEndpoint
from pyconnectwise.endpoints.manage.ServiceServiceSignoffEndpoint import ServiceServiceSignoffEndpoint
from pyconnectwise.endpoints.manage.ServiceSeveritiesEndpoint import ServiceSeveritiesEndpoint
from pyconnectwise.endpoints.manage.ServiceSLAsEndpoint import ServiceSLAsEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesEndpoint import ServiceSourcesEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysEndpoint import ServiceSurveysEndpoint
from pyconnectwise.endpoints.manage.ServiceTeamMembersEndpoint import ServiceTeamMembersEndpoint
from pyconnectwise.endpoints.manage.ServiceTeamsEndpoint import ServiceTeamsEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesEndpoint import ServiceTemplatesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketLinksEndpoint import ServiceTicketLinksEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsEndpoint import ServiceTicketsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketSyncsEndpoint import ServiceTicketSyncsEndpoint

class ServiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "service")
        
        self.boards = self._register_child_endpoint(
            ServiceBoardsEndpoint(client, parent_endpoint=self)
        )
        self.codes = self._register_child_endpoint(
            ServiceCodesEndpoint(client, parent_endpoint=self)
        )
        self.emailTemplates = self._register_child_endpoint(
            ServiceEmailTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.impacts = self._register_child_endpoint(
            ServiceImpactsEndpoint(client, parent_endpoint=self)
        )
        self.knowledgeBaseArticles = self._register_child_endpoint(
            ServiceKnowledgeBaseArticlesEndpoint(client, parent_endpoint=self)
        )
        self.knowledgeBaseCategories = self._register_child_endpoint(
            ServiceKnowledgeBaseCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.knowledgebasesettings = self._register_child_endpoint(
            ServiceKnowledgebasesettingsEndpoint(client, parent_endpoint=self)
        )
        self.knowledgeBaseSubCategories = self._register_child_endpoint(
            ServiceKnowledgeBaseSubCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.locations = self._register_child_endpoint(
            ServiceLocationsEndpoint(client, parent_endpoint=self)
        )
        self.priorities = self._register_child_endpoint(
            ServicePrioritiesEndpoint(client, parent_endpoint=self)
        )
        self.serviceSignoff = self._register_child_endpoint(
            ServiceServiceSignoffEndpoint(client, parent_endpoint=self)
        )
        self.severities = self._register_child_endpoint(
            ServiceSeveritiesEndpoint(client, parent_endpoint=self)
        )
        self.SLAs = self._register_child_endpoint(
            ServiceSLAsEndpoint(client, parent_endpoint=self)
        )
        self.sources = self._register_child_endpoint(
            ServiceSourcesEndpoint(client, parent_endpoint=self)
        )
        self.surveys = self._register_child_endpoint(
            ServiceSurveysEndpoint(client, parent_endpoint=self)
        )
        self.teamMembers = self._register_child_endpoint(
            ServiceTeamMembersEndpoint(client, parent_endpoint=self)
        )
        self.teams = self._register_child_endpoint(
            ServiceTeamsEndpoint(client, parent_endpoint=self)
        )
        self.templates = self._register_child_endpoint(
            ServiceTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.ticketLinks = self._register_child_endpoint(
            ServiceTicketLinksEndpoint(client, parent_endpoint=self)
        )
        self.tickets = self._register_child_endpoint(
            ServiceTicketsEndpoint(client, parent_endpoint=self)
        )
        self.ticketSyncs = self._register_child_endpoint(
            ServiceTicketSyncsEndpoint(client, parent_endpoint=self)
        )