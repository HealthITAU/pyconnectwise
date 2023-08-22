from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSurveysCountEndpoint import CompanyCompaniesIdSurveysCountEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesIdSurveysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "surveys", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyCompaniesIdSurveysCountEndpoint(client, parent_endpoint=self))
