from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingEndpoint import FinanceAccountingEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesEndpoint import FinanceAccountingpackagesEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesetupEndpoint import FinanceAccountingpackagesetupEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementrecapEndpoint import FinanceAgreementrecapEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsEndpoint import FinanceAgreementsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesEndpoint import FinanceAgreementtypesEndpoint
from pyconnectwise.endpoints.manage.FinanceBatchsetupsEndpoint import FinanceBatchsetupsEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingcyclesEndpoint import FinanceBillingcyclesEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsEndpoint import FinanceBillingsetupsEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingstatusesEndpoint import FinanceBillingstatusesEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingtermsEndpoint import FinanceBillingtermsEndpoint
from pyconnectwise.endpoints.manage.FinanceClosedinvoicesEndpoint import FinanceClosedinvoicesEndpoint
from pyconnectwise.endpoints.manage.FinanceCompanyfinanceEndpoint import FinanceCompanyfinanceEndpoint
from pyconnectwise.endpoints.manage.FinanceCurrenciesEndpoint import FinanceCurrenciesEndpoint
from pyconnectwise.endpoints.manage.FinanceDeliverymethodsEndpoint import FinanceDeliverymethodsEndpoint
from pyconnectwise.endpoints.manage.FinanceGlaccountsEndpoint import FinanceGlaccountsEndpoint
from pyconnectwise.endpoints.manage.FinanceGlcaptionsEndpoint import FinanceGlcaptionsEndpoint
from pyconnectwise.endpoints.manage.FinanceGlpathsEndpoint import FinanceGlpathsEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoEndpoint import FinanceInfoEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceemailtemplatesEndpoint import FinanceInvoiceemailtemplatesEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesEndpoint import FinanceInvoicesEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesEndpoint import FinanceInvoicetemplatesEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicetemplatesetupsEndpoint import FinanceInvoicetemplatesetupsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesEndpoint import FinanceTaxcodesEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxintegrationsEndpoint import FinanceTaxintegrationsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "finance", parent_endpoint=parent_endpoint)

        self.billing_statuses = self._register_child_endpoint(
            FinanceBillingstatusesEndpoint(client, parent_endpoint=self)
        )
        self.accounting = self._register_child_endpoint(FinanceAccountingEndpoint(client, parent_endpoint=self))
        self.invoices = self._register_child_endpoint(FinanceInvoicesEndpoint(client, parent_endpoint=self))
        self.invoice_email_templates = self._register_child_endpoint(
            FinanceInvoiceemailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.batch_setups = self._register_child_endpoint(FinanceBatchsetupsEndpoint(client, parent_endpoint=self))
        self.billing_setups = self._register_child_endpoint(FinanceBillingsetupsEndpoint(client, parent_endpoint=self))
        self.gl_captions = self._register_child_endpoint(FinanceGlcaptionsEndpoint(client, parent_endpoint=self))
        self.invoice_template_setups = self._register_child_endpoint(
            FinanceInvoicetemplatesetupsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(FinanceInfoEndpoint(client, parent_endpoint=self))
        self.invoice_templates = self._register_child_endpoint(
            FinanceInvoicetemplatesEndpoint(client, parent_endpoint=self)
        )
        self.glpaths = self._register_child_endpoint(FinanceGlpathsEndpoint(client, parent_endpoint=self))
        self.company_finance = self._register_child_endpoint(
            FinanceCompanyfinanceEndpoint(client, parent_endpoint=self)
        )
        self.tax_codes = self._register_child_endpoint(FinanceTaxcodesEndpoint(client, parent_endpoint=self))
        self.billing_terms = self._register_child_endpoint(FinanceBillingtermsEndpoint(client, parent_endpoint=self))
        self.accounting_packages = self._register_child_endpoint(
            FinanceAccountingpackagesEndpoint(client, parent_endpoint=self)
        )
        self.agreementrecap = self._register_child_endpoint(FinanceAgreementrecapEndpoint(client, parent_endpoint=self))
        self.delivery_methods = self._register_child_endpoint(
            FinanceDeliverymethodsEndpoint(client, parent_endpoint=self)
        )
        self.closed_invoices = self._register_child_endpoint(
            FinanceClosedinvoicesEndpoint(client, parent_endpoint=self)
        )
        self.agreements = self._register_child_endpoint(FinanceAgreementsEndpoint(client, parent_endpoint=self))
        self.gl_accounts = self._register_child_endpoint(FinanceGlaccountsEndpoint(client, parent_endpoint=self))
        self.billing_cycles = self._register_child_endpoint(FinanceBillingcyclesEndpoint(client, parent_endpoint=self))
        self.tax_integrations = self._register_child_endpoint(
            FinanceTaxintegrationsEndpoint(client, parent_endpoint=self)
        )
        self.currencies = self._register_child_endpoint(FinanceCurrenciesEndpoint(client, parent_endpoint=self))
        self.accounting_package_setup = self._register_child_endpoint(
            FinanceAccountingpackagesetupEndpoint(client, parent_endpoint=self)
        )
        self.agreement_types = self._register_child_endpoint(
            FinanceAgreementtypesEndpoint(client, parent_endpoint=self)
        )
