from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsyncCompanyEndpoint import (
    CompanyContactsyncCompanyEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsyncCompanysyncEndpoint import (
    CompanyContactsyncCompanysyncEndpoint,
)


class CompanyContactsyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "contactsync", parent_endpoint=parent_endpoint
        )

        self.company = self._register_child_endpoint(
            CompanyContactsyncCompanyEndpoint(client, parent_endpoint=self)
        )
        self.companysync = self._register_child_endpoint(
            CompanyContactsyncCompanysyncEndpoint(client, parent_endpoint=self)
        )
