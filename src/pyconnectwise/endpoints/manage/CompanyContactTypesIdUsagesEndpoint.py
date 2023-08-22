from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesIdUsagesListEndpoint import \
    CompanyContactTypesIdUsagesListEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactTypesIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "usages", parent_endpoint=parent_endpoint)

        self.list = self._register_child_endpoint(CompanyContactTypesIdUsagesListEndpoint(client, parent_endpoint=self))
