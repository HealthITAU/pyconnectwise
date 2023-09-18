from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesEndpoint import SalesActivitiesEndpoint
from pyconnectwise.endpoints.manage.SalesCommissionsEndpoint import SalesCommissionsEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesEndpoint import SalesOpportunitiesEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersEndpoint import SalesOrdersEndpoint
from pyconnectwise.endpoints.manage.SalesProbabilitiesEndpoint import SalesProbabilitiesEndpoint
from pyconnectwise.endpoints.manage.SalesQuotasEndpoint import SalesQuotasEndpoint
from pyconnectwise.endpoints.manage.SalesRolesEndpoint import SalesRolesEndpoint
from pyconnectwise.endpoints.manage.SalesSalesteamsEndpoint import SalesSalesteamsEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleEndpoint import SalesScheduleEndpoint
from pyconnectwise.endpoints.manage.SalesServiceEndpoint import SalesServiceEndpoint
from pyconnectwise.endpoints.manage.SalesStagesEndpoint import SalesStagesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sales", parent_endpoint=parent_endpoint)

        self.service = self._register_child_endpoint(SalesServiceEndpoint(client, parent_endpoint=self))
        self.sales_teams = self._register_child_endpoint(SalesSalesteamsEndpoint(client, parent_endpoint=self))
        self.roles = self._register_child_endpoint(SalesRolesEndpoint(client, parent_endpoint=self))
        self.probabilities = self._register_child_endpoint(SalesProbabilitiesEndpoint(client, parent_endpoint=self))
        self.commissions = self._register_child_endpoint(SalesCommissionsEndpoint(client, parent_endpoint=self))
        self.opportunities = self._register_child_endpoint(SalesOpportunitiesEndpoint(client, parent_endpoint=self))
        self.schedule = self._register_child_endpoint(SalesScheduleEndpoint(client, parent_endpoint=self))
        self.activities = self._register_child_endpoint(SalesActivitiesEndpoint(client, parent_endpoint=self))
        self.stages = self._register_child_endpoint(SalesStagesEndpoint(client, parent_endpoint=self))
        self.orders = self._register_child_endpoint(SalesOrdersEndpoint(client, parent_endpoint=self))
        self.quotas = self._register_child_endpoint(SalesQuotasEndpoint(client, parent_endpoint=self))
