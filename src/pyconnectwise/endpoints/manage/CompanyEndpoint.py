from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsEndpoint import CompanyAddressformatsEndpoint
from pyconnectwise.endpoints.manage.CompanyBillingsetupsEndpoint import CompanyBillingsetupsEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesEndpoint import CompanyCommunicationtypesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesEndpoint import CompanyCompaniesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanyfinanceEndpoint import CompanyCompanyfinanceEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanypickeritemsEndpoint import CompanyCompanypickeritemsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanytypeassociationsEndpoint import CompanyCompanytypeassociationsEndpoint
from pyconnectwise.endpoints.manage.CompanyConfigurationsEndpoint import CompanyConfigurationsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactEndpoint import CompanyContactEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsEndpoint import CompanyContactsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsyncEndpoint import CompanyContactsyncEndpoint
from pyconnectwise.endpoints.manage.CompanyContacttypeassociationsEndpoint import CompanyContacttypeassociationsEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesEndpoint import CompanyCountriesEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesEndpoint import CompanyEntitytypesEndpoint
from pyconnectwise.endpoints.manage.CompanyExpensetypesEndpoint import CompanyExpensetypesEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactEndpoint import CompanyM365contactEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncEndpoint import CompanyM365contactsyncEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsEndpoint import \
    CompanyManageddevicesintegrationsEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementbackupsEndpoint import CompanyManagementbackupsEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementEndpoint import CompanyManagementEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementitsolutionsEndpoint import CompanyManagementitsolutionsEndpoint
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsEndpoint import CompanyMarketdescriptionsEndpoint
from pyconnectwise.endpoints.manage.CompanyNotetypesEndpoint import CompanyNotetypesEndpoint
from pyconnectwise.endpoints.manage.CompanyOwnershiptypesEndpoint import CompanyOwnershiptypesEndpoint
from pyconnectwise.endpoints.manage.CompanyPaymenttypesEndpoint import CompanyPaymenttypesEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsEndpoint import CompanyPortalconfigurationsEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalsecuritylevelsEndpoint import CompanyPortalsecuritylevelsEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalsecuritysettingsEndpoint import CompanyPortalsecuritysettingsEndpoint
from pyconnectwise.endpoints.manage.CompanyStatesEndpoint import CompanyStatesEndpoint
from pyconnectwise.endpoints.manage.CompanyTeamrolesEndpoint import CompanyTeamrolesEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksEndpoint import CompanyTracksEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "company", parent_endpoint=parent_endpoint)

        self.companies = self._register_child_endpoint(CompanyCompaniesEndpoint(client, parent_endpoint=self))
        self.countries = self._register_child_endpoint(CompanyCountriesEndpoint(client, parent_endpoint=self))
        self.portal_security_settings = self._register_child_endpoint(
            CompanyPortalsecuritysettingsEndpoint(client, parent_endpoint=self)
        )
        self.ownership_types = self._register_child_endpoint(
            CompanyOwnershiptypesEndpoint(client, parent_endpoint=self)
        )
        self.company_picker_items = self._register_child_endpoint(
            CompanyCompanypickeritemsEndpoint(client, parent_endpoint=self)
        )
        self.contacts = self._register_child_endpoint(CompanyContactsEndpoint(client, parent_endpoint=self))
        self.management_backups = self._register_child_endpoint(
            CompanyManagementbackupsEndpoint(client, parent_endpoint=self)
        )
        self.billing_setups = self._register_child_endpoint(CompanyBillingsetupsEndpoint(client, parent_endpoint=self))
        self.entity_types = self._register_child_endpoint(CompanyEntitytypesEndpoint(client, parent_endpoint=self))
        self.portal_security_levels = self._register_child_endpoint(
            CompanyPortalsecuritylevelsEndpoint(client, parent_endpoint=self)
        )
        self.entitytypes = self._register_child_endpoint(CompanyEntitytypesEndpoint(client, parent_endpoint=self))
        self.company_type_associations = self._register_child_endpoint(
            CompanyCompanytypeassociationsEndpoint(client, parent_endpoint=self)
        )
        self.management = self._register_child_endpoint(CompanyManagementEndpoint(client, parent_endpoint=self))
        self.company_finance = self._register_child_endpoint(
            CompanyCompanyfinanceEndpoint(client, parent_endpoint=self)
        )
        self.note_types = self._register_child_endpoint(CompanyNotetypesEndpoint(client, parent_endpoint=self))
        self.states = self._register_child_endpoint(CompanyStatesEndpoint(client, parent_endpoint=self))
        self.managed_devices_integrations = self._register_child_endpoint(
            CompanyManageddevicesintegrationsEndpoint(client, parent_endpoint=self)
        )
        self.expense_types = self._register_child_endpoint(CompanyExpensetypesEndpoint(client, parent_endpoint=self))
        self.management_it_solutions = self._register_child_endpoint(
            CompanyManagementitsolutionsEndpoint(client, parent_endpoint=self)
        )
        self.team_roles = self._register_child_endpoint(CompanyTeamrolesEndpoint(client, parent_endpoint=self))
        self.market_descriptions = self._register_child_endpoint(
            CompanyMarketdescriptionsEndpoint(client, parent_endpoint=self)
        )
        self.contact = self._register_child_endpoint(CompanyContactEndpoint(client, parent_endpoint=self))
        self.m365contact = self._register_child_endpoint(CompanyM365contactEndpoint(client, parent_endpoint=self))
        self.contactsync = self._register_child_endpoint(CompanyContactsyncEndpoint(client, parent_endpoint=self))
        self.contact_type_associations = self._register_child_endpoint(
            CompanyContacttypeassociationsEndpoint(client, parent_endpoint=self)
        )
        self.communication_types = self._register_child_endpoint(
            CompanyCommunicationtypesEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self._register_child_endpoint(CompanyTracksEndpoint(client, parent_endpoint=self))
        self.payment_types = self._register_child_endpoint(CompanyPaymenttypesEndpoint(client, parent_endpoint=self))
        self.configurations = self._register_child_endpoint(CompanyConfigurationsEndpoint(client, parent_endpoint=self))
        self.address_formats = self._register_child_endpoint(
            CompanyAddressformatsEndpoint(client, parent_endpoint=self)
        )
        self.m365contactsync = self._register_child_endpoint(
            CompanyM365contactsyncEndpoint(client, parent_endpoint=self)
        )
        self.portal_configurations = self._register_child_endpoint(
            CompanyPortalconfigurationsEndpoint(client, parent_endpoint=self)
        )
