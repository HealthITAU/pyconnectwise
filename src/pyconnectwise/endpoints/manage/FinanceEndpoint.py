from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingPackagesEndpoint import FinanceAccountingPackagesEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingPackageSetupEndpoint import FinanceAccountingPackageSetupEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsEndpoint import FinanceAgreementsEndpoint
from pyconnectwise.endpoints.manage.FinanceBatchSetupsEndpoint import FinanceBatchSetupsEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingCyclesEndpoint import FinanceBillingCyclesEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingSetupsEndpoint import FinanceBillingSetupsEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingStatusesEndpoint import FinanceBillingStatusesEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingTermsEndpoint import FinanceBillingTermsEndpoint
from pyconnectwise.endpoints.manage.FinanceCurrenciesEndpoint import FinanceCurrenciesEndpoint
from pyconnectwise.endpoints.manage.FinanceDeliveryMethodsEndpoint import FinanceDeliveryMethodsEndpoint
from pyconnectwise.endpoints.manage.FinanceGlAccountsEndpoint import FinanceGlAccountsEndpoint
from pyconnectwise.endpoints.manage.FinanceGlCaptionsEndpoint import FinanceGlCaptionsEndpoint
from pyconnectwise.endpoints.manage.FinanceGlpathsEndpoint import FinanceGlpathsEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceEmailTemplatesEndpoint import FinanceInvoiceEmailTemplatesEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesEndpoint import FinanceInvoicesEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceTemplatesEndpoint import FinanceInvoiceTemplatesEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceTemplateSetupsEndpoint import FinanceInvoiceTemplateSetupsEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesEndpoint import FinanceTaxCodesEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxIntegrationsEndpoint import FinanceTaxIntegrationsEndpoint

class FinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "finance")
        
        self.accountingPackages = self._register_child_endpoint(
            FinanceAccountingPackagesEndpoint(client, parent_endpoint=self)
        )
        self.accountingPackageSetup = self._register_child_endpoint(
            FinanceAccountingPackageSetupEndpoint(client, parent_endpoint=self)
        )
        self.agreements = self._register_child_endpoint(
            FinanceAgreementsEndpoint(client, parent_endpoint=self)
        )
        self.batchSetups = self._register_child_endpoint(
            FinanceBatchSetupsEndpoint(client, parent_endpoint=self)
        )
        self.billingCycles = self._register_child_endpoint(
            FinanceBillingCyclesEndpoint(client, parent_endpoint=self)
        )
        self.billingSetups = self._register_child_endpoint(
            FinanceBillingSetupsEndpoint(client, parent_endpoint=self)
        )
        self.billingStatuses = self._register_child_endpoint(
            FinanceBillingStatusesEndpoint(client, parent_endpoint=self)
        )
        self.billingTerms = self._register_child_endpoint(
            FinanceBillingTermsEndpoint(client, parent_endpoint=self)
        )
        self.currencies = self._register_child_endpoint(
            FinanceCurrenciesEndpoint(client, parent_endpoint=self)
        )
        self.deliveryMethods = self._register_child_endpoint(
            FinanceDeliveryMethodsEndpoint(client, parent_endpoint=self)
        )
        self.glAccounts = self._register_child_endpoint(
            FinanceGlAccountsEndpoint(client, parent_endpoint=self)
        )
        self.glCaptions = self._register_child_endpoint(
            FinanceGlCaptionsEndpoint(client, parent_endpoint=self)
        )
        self.glpaths = self._register_child_endpoint(
            FinanceGlpathsEndpoint(client, parent_endpoint=self)
        )
        self.invoiceEmailTemplates = self._register_child_endpoint(
            FinanceInvoiceEmailTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.invoices = self._register_child_endpoint(
            FinanceInvoicesEndpoint(client, parent_endpoint=self)
        )
        self.invoiceTemplates = self._register_child_endpoint(
            FinanceInvoiceTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.invoiceTemplateSetups = self._register_child_endpoint(
            FinanceInvoiceTemplateSetupsEndpoint(client, parent_endpoint=self)
        )
        self.taxCodes = self._register_child_endpoint(
            FinanceTaxCodesEndpoint(client, parent_endpoint=self)
        )
        self.taxIntegrations = self._register_child_endpoint(
            FinanceTaxIntegrationsEndpoint(client, parent_endpoint=self)
        )