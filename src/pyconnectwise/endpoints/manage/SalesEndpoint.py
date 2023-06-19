from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesEndpoint import SalesActivitiesEndpoint
from pyconnectwise.endpoints.manage.SalesCommissionsEndpoint import SalesCommissionsEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesEndpoint import SalesOpportunitiesEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersEndpoint import SalesOrdersEndpoint
from pyconnectwise.endpoints.manage.SalesProbabilitiesEndpoint import SalesProbabilitiesEndpoint
from pyconnectwise.endpoints.manage.SalesQuotasEndpoint import SalesQuotasEndpoint
from pyconnectwise.endpoints.manage.SalesRolesEndpoint import SalesRolesEndpoint
from pyconnectwise.endpoints.manage.SalesSalesTeamsEndpoint import SalesSalesTeamsEndpoint
from pyconnectwise.endpoints.manage.SalesStagesEndpoint import SalesStagesEndpoint

class SalesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "sales")
        
        self.activities = self.register_child_endpoint(
            SalesActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.commissions = self.register_child_endpoint(
            SalesCommissionsEndpoint(client, parent_endpoint=self)
        )
        self.opportunities = self.register_child_endpoint(
            SalesOpportunitiesEndpoint(client, parent_endpoint=self)
        )
        self.orders = self.register_child_endpoint(
            SalesOrdersEndpoint(client, parent_endpoint=self)
        )
        self.probabilities = self.register_child_endpoint(
            SalesProbabilitiesEndpoint(client, parent_endpoint=self)
        )
        self.quotas = self.register_child_endpoint(
            SalesQuotasEndpoint(client, parent_endpoint=self)
        )
        self.roles = self.register_child_endpoint(
            SalesRolesEndpoint(client, parent_endpoint=self)
        )
        self.salesTeams = self.register_child_endpoint(
            SalesSalesTeamsEndpoint(client, parent_endpoint=self)
        )
        self.stages = self.register_child_endpoint(
            SalesStagesEndpoint(client, parent_endpoint=self)
        )