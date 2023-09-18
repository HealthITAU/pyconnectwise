from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAllowedfiletypesEndpoint import SystemAllowedfiletypesEndpoint
from pyconnectwise.endpoints.manage.SystemAllowedoriginsEndpoint import SystemAllowedoriginsEndpoint
from pyconnectwise.endpoints.manage.SystemApimembersEndpoint import SystemApimembersEndpoint
from pyconnectwise.endpoints.manage.SystemAudittrailEndpoint import SystemAudittrailEndpoint
from pyconnectwise.endpoints.manage.SystemAuthanvilsEndpoint import SystemAuthanvilsEndpoint
from pyconnectwise.endpoints.manage.SystemAutosynctimeEndpoint import SystemAutosynctimeEndpoint
from pyconnectwise.endpoints.manage.SystemBundlesEndpoint import SystemBundlesEndpoint
from pyconnectwise.endpoints.manage.SystemCallbacksEndpoint import SystemCallbacksEndpoint
from pyconnectwise.endpoints.manage.SystemCertificationsEndpoint import SystemCertificationsEndpoint
from pyconnectwise.endpoints.manage.SystemConnectwisehostedscreensEndpoint import SystemConnectwisehostedscreensEndpoint
from pyconnectwise.endpoints.manage.SystemConnectwisehostedsetupsEndpoint import SystemConnectwisehostedsetupsEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncEndpoint import SystemContactsyncEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsEndpoint import SystemCustomreportsEndpoint
from pyconnectwise.endpoints.manage.SystemCwtimezonesEndpoint import SystemCwtimezonesEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsEndpoint import SystemDepartmentsEndpoint
from pyconnectwise.endpoints.manage.SystemDirectionalsyncsEndpoint import SystemDirectionalsyncsEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsEndpoint import SystemDocumentsEndpoint
from pyconnectwise.endpoints.manage.SystemDocumenttypesEndpoint import SystemDocumenttypesEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsEndpoint import SystemEmailconnectorsEndpoint
from pyconnectwise.endpoints.manage.SystemEmailexclusionsEndpoint import SystemEmailexclusionsEndpoint
from pyconnectwise.endpoints.manage.SystemEmailtokensEndpoint import SystemEmailtokensEndpoint
from pyconnectwise.endpoints.manage.SystemEpayconfigurationsEndpoint import SystemEpayconfigurationsEndpoint
from pyconnectwise.endpoints.manage.SystemExperimentsEndpoint import SystemExperimentsEndpoint
from pyconnectwise.endpoints.manage.SystemFileuploadsettingsEndpoint import SystemFileuploadsettingsEndpoint
from pyconnectwise.endpoints.manage.SystemGoogleemailsetupEndpoint import SystemGoogleemailsetupEndpoint
from pyconnectwise.endpoints.manage.SystemImapsEndpoint import SystemImapsEndpoint
from pyconnectwise.endpoints.manage.SystemImportmassmaintenanceEndpoint import SystemImportmassmaintenanceEndpoint
from pyconnectwise.endpoints.manage.SystemInfoEndpoint import SystemInfoEndpoint
from pyconnectwise.endpoints.manage.SystemInoutboardsEndpoint import SystemInoutboardsEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesEndpoint import SystemInouttypesEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorloginsEndpoint import SystemIntegratorloginsEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratortagsEndpoint import SystemIntegratortagsEndpoint
from pyconnectwise.endpoints.manage.SystemKpicategoriesEndpoint import SystemKpicategoriesEndpoint
from pyconnectwise.endpoints.manage.SystemKpisEndpoint import SystemKpisEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsEndpoint import SystemLdapconfigurationsEndpoint
from pyconnectwise.endpoints.manage.SystemLinksEndpoint import SystemLinksEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsEndpoint import SystemLocationsEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncEndpoint import SystemM365contactsyncEndpoint
from pyconnectwise.endpoints.manage.SystemManagementnetworksecuritiesEndpoint import \
    SystemManagementnetworksecuritiesEndpoint
from pyconnectwise.endpoints.manage.SystemMarketplaceimportEndpoint import SystemMarketplaceimportEndpoint
from pyconnectwise.endpoints.manage.SystemMembersEndpoint import SystemMembersEndpoint
from pyconnectwise.endpoints.manage.SystemMembertemplatesEndpoint import SystemMembertemplatesEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesEndpoint import SystemMenuentriesEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountEndpoint import SystemMyaccountEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyEndpoint import SystemMycompanyEndpoint
from pyconnectwise.endpoints.manage.SystemMymembersEndpoint import SystemMymembersEndpoint
from pyconnectwise.endpoints.manage.SystemMysecurityEndpoint import SystemMysecurityEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationrecipientsEndpoint import SystemNotificationrecipientsEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365Endpoint import SystemOffice365Endpoint
from pyconnectwise.endpoints.manage.SystemOnpremisesearchsettingEndpoint import SystemOnpremisesearchsettingEndpoint
from pyconnectwise.endpoints.manage.SystemOsgradeweightsEndpoint import SystemOsgradeweightsEndpoint
from pyconnectwise.endpoints.manage.SystemParsingtypesEndpoint import SystemParsingtypesEndpoint
from pyconnectwise.endpoints.manage.SystemParsingvariablesEndpoint import SystemParsingvariablesEndpoint
from pyconnectwise.endpoints.manage.SystemPortalreportsEndpoint import SystemPortalreportsEndpoint
from pyconnectwise.endpoints.manage.SystemQuotelinksetupEndpoint import SystemQuotelinksetupEndpoint
from pyconnectwise.endpoints.manage.SystemReportcardsEndpoint import SystemReportcardsEndpoint
from pyconnectwise.endpoints.manage.SystemReportsEndpoint import SystemReportsEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesEndpoint import SystemSecurityrolesEndpoint
from pyconnectwise.endpoints.manage.SystemSettingsEndpoint import SystemSettingsEndpoint
from pyconnectwise.endpoints.manage.SystemSetupscreensEndpoint import SystemSetupscreensEndpoint
from pyconnectwise.endpoints.manage.SystemSkillcategoriesEndpoint import SystemSkillcategoriesEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsEndpoint import SystemSkillsEndpoint
from pyconnectwise.endpoints.manage.SystemSsoconfigurationsEndpoint import SystemSsoconfigurationsEndpoint
from pyconnectwise.endpoints.manage.SystemSsousersEndpoint import SystemSsousersEndpoint
from pyconnectwise.endpoints.manage.SystemStandardnotesEndpoint import SystemStandardnotesEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysEndpoint import SystemSurveysEndpoint
from pyconnectwise.endpoints.manage.SystemTimezonesetupsEndpoint import SystemTimezonesetupsEndpoint
from pyconnectwise.endpoints.manage.SystemTodaypagecategoriesEndpoint import SystemTodaypagecategoriesEndpoint
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsEndpoint import SystemUserdefinedfieldsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowactionsEndpoint import SystemWorkflowactionsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsEndpoint import SystemWorkflowsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "system", parent_endpoint=parent_endpoint)

        self.auth_anvils = self._register_child_endpoint(SystemAuthanvilsEndpoint(client, parent_endpoint=self))
        self.documents = self._register_child_endpoint(SystemDocumentsEndpoint(client, parent_endpoint=self))
        self.departments = self._register_child_endpoint(SystemDepartmentsEndpoint(client, parent_endpoint=self))
        self.in_out_boards = self._register_child_endpoint(SystemInoutboardsEndpoint(client, parent_endpoint=self))
        self.email_tokens = self._register_child_endpoint(SystemEmailtokensEndpoint(client, parent_endpoint=self))
        self.on_premise_search_setting = self._register_child_endpoint(
            SystemOnpremisesearchsettingEndpoint(client, parent_endpoint=self)
        )
        self.standard_notes = self._register_child_endpoint(SystemStandardnotesEndpoint(client, parent_endpoint=self))
        self.workflow_actions = self._register_child_endpoint(
            SystemWorkflowactionsEndpoint(client, parent_endpoint=self)
        )
        self.cw_time_zones = self._register_child_endpoint(SystemCwtimezonesEndpoint(client, parent_endpoint=self))
        self.my_security = self._register_child_endpoint(SystemMysecurityEndpoint(client, parent_endpoint=self))
        self.allowed_file_types = self._register_child_endpoint(
            SystemAllowedfiletypesEndpoint(client, parent_endpoint=self)
        )
        self.parsing_types = self._register_child_endpoint(SystemParsingtypesEndpoint(client, parent_endpoint=self))
        self.allowedorigins = self._register_child_endpoint(SystemAllowedoriginsEndpoint(client, parent_endpoint=self))
        self.document_types = self._register_child_endpoint(SystemDocumenttypesEndpoint(client, parent_endpoint=self))
        self.email_connectors = self._register_child_endpoint(
            SystemEmailconnectorsEndpoint(client, parent_endpoint=self)
        )
        self.custom_reports = self._register_child_endpoint(SystemCustomreportsEndpoint(client, parent_endpoint=self))
        self.management_network_securities = self._register_child_endpoint(
            SystemManagementnetworksecuritiesEndpoint(client, parent_endpoint=self)
        )
        self.e_pay_configurations = self._register_child_endpoint(
            SystemEpayconfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.import_mass_maintenance = self._register_child_endpoint(
            SystemImportmassmaintenanceEndpoint(client, parent_endpoint=self)
        )
        self.members = self._register_child_endpoint(SystemMembersEndpoint(client, parent_endpoint=self))
        self.quote_link_setup = self._register_child_endpoint(
            SystemQuotelinksetupEndpoint(client, parent_endpoint=self)
        )
        self.integrator_tags = self._register_child_endpoint(SystemIntegratortagsEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemInfoEndpoint(client, parent_endpoint=self))
        self.callbacks = self._register_child_endpoint(SystemCallbacksEndpoint(client, parent_endpoint=self))
        self.report_cards = self._register_child_endpoint(SystemReportcardsEndpoint(client, parent_endpoint=self))
        self.audittrail = self._register_child_endpoint(SystemAudittrailEndpoint(client, parent_endpoint=self))
        self.time_zone_setups = self._register_child_endpoint(
            SystemTimezonesetupsEndpoint(client, parent_endpoint=self)
        )
        self.imaps = self._register_child_endpoint(SystemImapsEndpoint(client, parent_endpoint=self))
        self.user_defined_fields = self._register_child_endpoint(
            SystemUserdefinedfieldsEndpoint(client, parent_endpoint=self)
        )
        self.setup_screens = self._register_child_endpoint(SystemSetupscreensEndpoint(client, parent_endpoint=self))
        self.fileuploadsettings = self._register_child_endpoint(
            SystemFileuploadsettingsEndpoint(client, parent_endpoint=self)
        )
        self.kpi_categories = self._register_child_endpoint(SystemKpicategoriesEndpoint(client, parent_endpoint=self))
        self.in_out_types = self._register_child_endpoint(SystemInouttypesEndpoint(client, parent_endpoint=self))
        self.integratorlogins = self._register_child_endpoint(
            SystemIntegratorloginsEndpoint(client, parent_endpoint=self)
        )
        self.membertemplates = self._register_child_endpoint(
            SystemMembertemplatesEndpoint(client, parent_endpoint=self)
        )
        self.allowedfiletypes = self._register_child_endpoint(
            SystemAllowedfiletypesEndpoint(client, parent_endpoint=self)
        )
        self.skill_categories = self._register_child_endpoint(
            SystemSkillcategoriesEndpoint(client, parent_endpoint=self)
        )
        self.api_members = self._register_child_endpoint(SystemApimembersEndpoint(client, parent_endpoint=self))
        self.security_roles = self._register_child_endpoint(SystemSecurityrolesEndpoint(client, parent_endpoint=self))
        self.settings = self._register_child_endpoint(SystemSettingsEndpoint(client, parent_endpoint=self))
        self.mycompany = self._register_child_endpoint(SystemMycompanyEndpoint(client, parent_endpoint=self))
        self.notification_recipients = self._register_child_endpoint(
            SystemNotificationrecipientsEndpoint(client, parent_endpoint=self)
        )
        self.workflows = self._register_child_endpoint(SystemWorkflowsEndpoint(client, parent_endpoint=self))
        self.auto_sync_time = self._register_child_endpoint(SystemAutosynctimeEndpoint(client, parent_endpoint=self))
        self.email_exclusions = self._register_child_endpoint(
            SystemEmailexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.my_account = self._register_child_endpoint(SystemMyaccountEndpoint(client, parent_endpoint=self))
        self.parsing_variables = self._register_child_endpoint(
            SystemParsingvariablesEndpoint(client, parent_endpoint=self)
        )
        self.m365contactsync = self._register_child_endpoint(
            SystemM365contactsyncEndpoint(client, parent_endpoint=self)
        )
        self.sso_configurations = self._register_child_endpoint(
            SystemSsoconfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.connect_wise_hosted_screens = self._register_child_endpoint(
            SystemConnectwisehostedscreensEndpoint(client, parent_endpoint=self)
        )
        self.osgradeweights = self._register_child_endpoint(SystemOsgradeweightsEndpoint(client, parent_endpoint=self))
        self.securityroles = self._register_child_endpoint(SystemSecurityrolesEndpoint(client, parent_endpoint=self))
        self.certifications = self._register_child_endpoint(SystemCertificationsEndpoint(client, parent_endpoint=self))
        self.reports = self._register_child_endpoint(SystemReportsEndpoint(client, parent_endpoint=self))
        self.portal_reports = self._register_child_endpoint(SystemPortalreportsEndpoint(client, parent_endpoint=self))
        self.contactsync = self._register_child_endpoint(SystemContactsyncEndpoint(client, parent_endpoint=self))
        self.ldap_configurations = self._register_child_endpoint(
            SystemLdapconfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.skills = self._register_child_endpoint(SystemSkillsEndpoint(client, parent_endpoint=self))
        self.kpis = self._register_child_endpoint(SystemKpisEndpoint(client, parent_endpoint=self))
        self.menuentries = self._register_child_endpoint(SystemMenuentriesEndpoint(client, parent_endpoint=self))
        self.my_members = self._register_child_endpoint(SystemMymembersEndpoint(client, parent_endpoint=self))
        self.googleemailsetup = self._register_child_endpoint(
            SystemGoogleemailsetupEndpoint(client, parent_endpoint=self)
        )
        self.my_company = self._register_child_endpoint(SystemMycompanyEndpoint(client, parent_endpoint=self))
        self.experiments = self._register_child_endpoint(SystemExperimentsEndpoint(client, parent_endpoint=self))
        self.today_page_categories = self._register_child_endpoint(
            SystemTodaypagecategoriesEndpoint(client, parent_endpoint=self)
        )
        self.links = self._register_child_endpoint(SystemLinksEndpoint(client, parent_endpoint=self))
        self.marketplaceimport = self._register_child_endpoint(
            SystemMarketplaceimportEndpoint(client, parent_endpoint=self)
        )
        self.menu_entries = self._register_child_endpoint(SystemMenuentriesEndpoint(client, parent_endpoint=self))
        self.directional_syncs = self._register_child_endpoint(
            SystemDirectionalsyncsEndpoint(client, parent_endpoint=self)
        )
        self.sso_users = self._register_child_endpoint(SystemSsousersEndpoint(client, parent_endpoint=self))
        self.bundles = self._register_child_endpoint(SystemBundlesEndpoint(client, parent_endpoint=self))
        self.connectwisehostedsetups = self._register_child_endpoint(
            SystemConnectwisehostedsetupsEndpoint(client, parent_endpoint=self)
        )
        self.locations = self._register_child_endpoint(SystemLocationsEndpoint(client, parent_endpoint=self))
        self.surveys = self._register_child_endpoint(SystemSurveysEndpoint(client, parent_endpoint=self))
        self.office365 = self._register_child_endpoint(SystemOffice365Endpoint(client, parent_endpoint=self))
