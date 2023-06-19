from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAllowedoriginsEndpoint import SystemAllowedoriginsEndpoint
from pyconnectwise.endpoints.manage.SystemApiMembersEndpoint import SystemApiMembersEndpoint
from pyconnectwise.endpoints.manage.SystemAudittrailEndpoint import SystemAudittrailEndpoint
from pyconnectwise.endpoints.manage.SystemAuthAnvilsEndpoint import SystemAuthAnvilsEndpoint
from pyconnectwise.endpoints.manage.SystemAutoSyncTimeEndpoint import SystemAutoSyncTimeEndpoint
from pyconnectwise.endpoints.manage.SystemBundlesEndpoint import SystemBundlesEndpoint
from pyconnectwise.endpoints.manage.SystemCallbacksEndpoint import SystemCallbacksEndpoint
from pyconnectwise.endpoints.manage.SystemCertificationsEndpoint import SystemCertificationsEndpoint
from pyconnectwise.endpoints.manage.SystemConnectWiseHostedScreensEndpoint import SystemConnectWiseHostedScreensEndpoint
from pyconnectwise.endpoints.manage.SystemConnectwisehostedsetupsEndpoint import SystemConnectwisehostedsetupsEndpoint
from pyconnectwise.endpoints.manage.SystemCustomReportsEndpoint import SystemCustomReportsEndpoint
from pyconnectwise.endpoints.manage.SystemCwTimeZonesEndpoint import SystemCwTimeZonesEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsEndpoint import SystemDepartmentsEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsEndpoint import SystemDocumentsEndpoint
from pyconnectwise.endpoints.manage.SystemEmailConnectorsEndpoint import SystemEmailConnectorsEndpoint
from pyconnectwise.endpoints.manage.SystemEmailExclusionsEndpoint import SystemEmailExclusionsEndpoint
from pyconnectwise.endpoints.manage.SystemEmailTokensEndpoint import SystemEmailTokensEndpoint
from pyconnectwise.endpoints.manage.SystemEPayConfigurationsEndpoint import SystemEPayConfigurationsEndpoint
from pyconnectwise.endpoints.manage.SystemExperimentsEndpoint import SystemExperimentsEndpoint
from pyconnectwise.endpoints.manage.SystemImapsEndpoint import SystemImapsEndpoint
from pyconnectwise.endpoints.manage.SystemInfoEndpoint import SystemInfoEndpoint
from pyconnectwise.endpoints.manage.SystemInOutBoardsEndpoint import SystemInOutBoardsEndpoint
from pyconnectwise.endpoints.manage.SystemInOutTypesEndpoint import SystemInOutTypesEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorloginsEndpoint import SystemIntegratorloginsEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorTagsEndpoint import SystemIntegratorTagsEndpoint
from pyconnectwise.endpoints.manage.SystemKpiCategoriesEndpoint import SystemKpiCategoriesEndpoint
from pyconnectwise.endpoints.manage.SystemKpisEndpoint import SystemKpisEndpoint
from pyconnectwise.endpoints.manage.SystemLdapConfigurationsEndpoint import SystemLdapConfigurationsEndpoint
from pyconnectwise.endpoints.manage.SystemLinksEndpoint import SystemLinksEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsEndpoint import SystemLocationsEndpoint
from pyconnectwise.endpoints.manage.SystemManagementNetworkSecuritiesEndpoint import SystemManagementNetworkSecuritiesEndpoint
from pyconnectwise.endpoints.manage.SystemMembersEndpoint import SystemMembersEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesEndpoint import SystemMenuentriesEndpoint
from pyconnectwise.endpoints.manage.SystemMyMembersEndpoint import SystemMyMembersEndpoint
from pyconnectwise.endpoints.manage.SystemMySecurityEndpoint import SystemMySecurityEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationRecipientsEndpoint import SystemNotificationRecipientsEndpoint
from pyconnectwise.endpoints.manage.SystemOsgradeweightsEndpoint import SystemOsgradeweightsEndpoint
from pyconnectwise.endpoints.manage.SystemParsingTypesEndpoint import SystemParsingTypesEndpoint
from pyconnectwise.endpoints.manage.SystemParsingVariablesEndpoint import SystemParsingVariablesEndpoint
from pyconnectwise.endpoints.manage.SystemPortalReportsEndpoint import SystemPortalReportsEndpoint
from pyconnectwise.endpoints.manage.SystemQuoteLinkSetupEndpoint import SystemQuoteLinkSetupEndpoint
from pyconnectwise.endpoints.manage.SystemReportCardsEndpoint import SystemReportCardsEndpoint
from pyconnectwise.endpoints.manage.SystemReportsEndpoint import SystemReportsEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesEndpoint import SystemSecurityrolesEndpoint
from pyconnectwise.endpoints.manage.SystemSettingsEndpoint import SystemSettingsEndpoint
from pyconnectwise.endpoints.manage.SystemSetupScreensEndpoint import SystemSetupScreensEndpoint
from pyconnectwise.endpoints.manage.SystemSkillCategoriesEndpoint import SystemSkillCategoriesEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsEndpoint import SystemSkillsEndpoint
from pyconnectwise.endpoints.manage.SystemSsoConfigurationsEndpoint import SystemSsoConfigurationsEndpoint
from pyconnectwise.endpoints.manage.SystemSsoUsersEndpoint import SystemSsoUsersEndpoint
from pyconnectwise.endpoints.manage.SystemStandardNotesEndpoint import SystemStandardNotesEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysEndpoint import SystemSurveysEndpoint
from pyconnectwise.endpoints.manage.SystemTimeZoneSetupsEndpoint import SystemTimeZoneSetupsEndpoint
from pyconnectwise.endpoints.manage.SystemTodayPageCategoriesEndpoint import SystemTodayPageCategoriesEndpoint
from pyconnectwise.endpoints.manage.SystemUserDefinedFieldsEndpoint import SystemUserDefinedFieldsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsEndpoint import SystemWorkflowsEndpoint

class SystemEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "system")
        
        self.allowedorigins = self.register_child_endpoint(
            SystemAllowedoriginsEndpoint(client, parent_endpoint=self)
        )
        self.apiMembers = self.register_child_endpoint(
            SystemApiMembersEndpoint(client, parent_endpoint=self)
        )
        self.audittrail = self.register_child_endpoint(
            SystemAudittrailEndpoint(client, parent_endpoint=self)
        )
        self.authAnvils = self.register_child_endpoint(
            SystemAuthAnvilsEndpoint(client, parent_endpoint=self)
        )
        self.autoSyncTime = self.register_child_endpoint(
            SystemAutoSyncTimeEndpoint(client, parent_endpoint=self)
        )
        self.bundles = self.register_child_endpoint(
            SystemBundlesEndpoint(client, parent_endpoint=self)
        )
        self.callbacks = self.register_child_endpoint(
            SystemCallbacksEndpoint(client, parent_endpoint=self)
        )
        self.certifications = self.register_child_endpoint(
            SystemCertificationsEndpoint(client, parent_endpoint=self)
        )
        self.connectWiseHostedScreens = self.register_child_endpoint(
            SystemConnectWiseHostedScreensEndpoint(client, parent_endpoint=self)
        )
        self.connectwisehostedsetups = self.register_child_endpoint(
            SystemConnectwisehostedsetupsEndpoint(client, parent_endpoint=self)
        )
        self.customReports = self.register_child_endpoint(
            SystemCustomReportsEndpoint(client, parent_endpoint=self)
        )
        self.cwTimeZones = self.register_child_endpoint(
            SystemCwTimeZonesEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            SystemDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.documents = self.register_child_endpoint(
            SystemDocumentsEndpoint(client, parent_endpoint=self)
        )
        self.emailConnectors = self.register_child_endpoint(
            SystemEmailConnectorsEndpoint(client, parent_endpoint=self)
        )
        self.emailExclusions = self.register_child_endpoint(
            SystemEmailExclusionsEndpoint(client, parent_endpoint=self)
        )
        self.emailTokens = self.register_child_endpoint(
            SystemEmailTokensEndpoint(client, parent_endpoint=self)
        )
        self.ePayConfigurations = self.register_child_endpoint(
            SystemEPayConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.experiments = self.register_child_endpoint(
            SystemExperimentsEndpoint(client, parent_endpoint=self)
        )
        self.imaps = self.register_child_endpoint(
            SystemImapsEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemInfoEndpoint(client, parent_endpoint=self)
        )
        self.inOutBoards = self.register_child_endpoint(
            SystemInOutBoardsEndpoint(client, parent_endpoint=self)
        )
        self.inOutTypes = self.register_child_endpoint(
            SystemInOutTypesEndpoint(client, parent_endpoint=self)
        )
        self.integratorlogins = self.register_child_endpoint(
            SystemIntegratorloginsEndpoint(client, parent_endpoint=self)
        )
        self.integratorTags = self.register_child_endpoint(
            SystemIntegratorTagsEndpoint(client, parent_endpoint=self)
        )
        self.kpiCategories = self.register_child_endpoint(
            SystemKpiCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.kpis = self.register_child_endpoint(
            SystemKpisEndpoint(client, parent_endpoint=self)
        )
        self.ldapConfigurations = self.register_child_endpoint(
            SystemLdapConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.links = self.register_child_endpoint(
            SystemLinksEndpoint(client, parent_endpoint=self)
        )
        self.locations = self.register_child_endpoint(
            SystemLocationsEndpoint(client, parent_endpoint=self)
        )
        self.managementNetworkSecurities = self.register_child_endpoint(
            SystemManagementNetworkSecuritiesEndpoint(client, parent_endpoint=self)
        )
        self.members = self.register_child_endpoint(
            SystemMembersEndpoint(client, parent_endpoint=self)
        )
        self.menuentries = self.register_child_endpoint(
            SystemMenuentriesEndpoint(client, parent_endpoint=self)
        )
        self.myMembers = self.register_child_endpoint(
            SystemMyMembersEndpoint(client, parent_endpoint=self)
        )
        self.mySecurity = self.register_child_endpoint(
            SystemMySecurityEndpoint(client, parent_endpoint=self)
        )
        self.notificationRecipients = self.register_child_endpoint(
            SystemNotificationRecipientsEndpoint(client, parent_endpoint=self)
        )
        self.osgradeweights = self.register_child_endpoint(
            SystemOsgradeweightsEndpoint(client, parent_endpoint=self)
        )
        self.parsingTypes = self.register_child_endpoint(
            SystemParsingTypesEndpoint(client, parent_endpoint=self)
        )
        self.parsingVariables = self.register_child_endpoint(
            SystemParsingVariablesEndpoint(client, parent_endpoint=self)
        )
        self.portalReports = self.register_child_endpoint(
            SystemPortalReportsEndpoint(client, parent_endpoint=self)
        )
        self.quoteLinkSetup = self.register_child_endpoint(
            SystemQuoteLinkSetupEndpoint(client, parent_endpoint=self)
        )
        self.reportCards = self.register_child_endpoint(
            SystemReportCardsEndpoint(client, parent_endpoint=self)
        )
        self.reports = self.register_child_endpoint(
            SystemReportsEndpoint(client, parent_endpoint=self)
        )
        self.securityroles = self.register_child_endpoint(
            SystemSecurityrolesEndpoint(client, parent_endpoint=self)
        )
        self.settings = self.register_child_endpoint(
            SystemSettingsEndpoint(client, parent_endpoint=self)
        )
        self.setupScreens = self.register_child_endpoint(
            SystemSetupScreensEndpoint(client, parent_endpoint=self)
        )
        self.skillCategories = self.register_child_endpoint(
            SystemSkillCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.skills = self.register_child_endpoint(
            SystemSkillsEndpoint(client, parent_endpoint=self)
        )
        self.ssoConfigurations = self.register_child_endpoint(
            SystemSsoConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.ssoUsers = self.register_child_endpoint(
            SystemSsoUsersEndpoint(client, parent_endpoint=self)
        )
        self.standardNotes = self.register_child_endpoint(
            SystemStandardNotesEndpoint(client, parent_endpoint=self)
        )
        self.surveys = self.register_child_endpoint(
            SystemSurveysEndpoint(client, parent_endpoint=self)
        )
        self.timeZoneSetups = self.register_child_endpoint(
            SystemTimeZoneSetupsEndpoint(client, parent_endpoint=self)
        )
        self.todayPageCategories = self.register_child_endpoint(
            SystemTodayPageCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.userDefinedFields = self.register_child_endpoint(
            SystemUserDefinedFieldsEndpoint(client, parent_endpoint=self)
        )
        self.workflows = self.register_child_endpoint(
            SystemWorkflowsEndpoint(client, parent_endpoint=self)
        )