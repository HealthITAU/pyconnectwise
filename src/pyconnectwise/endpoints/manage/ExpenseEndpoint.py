from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseClassificationsEndpoint import ExpenseClassificationsEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesEndpoint import ExpenseEntriesEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymentTypesEndpoint import ExpensePaymentTypesEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsEndpoint import ExpenseReportsEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesEndpoint import ExpenseTypesEndpoint

class ExpenseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "expense")
        
        self.classifications = self.register_child_endpoint(
            ExpenseClassificationsEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            ExpenseEntriesEndpoint(client, parent_endpoint=self)
        )
        self.paymentTypes = self.register_child_endpoint(
            ExpensePaymentTypesEndpoint(client, parent_endpoint=self)
        )
        self.reports = self.register_child_endpoint(
            ExpenseReportsEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ExpenseTypesEndpoint(client, parent_endpoint=self)
        )