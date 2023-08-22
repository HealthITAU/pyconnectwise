from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesIdUsagesEndpoint import CompanyContactTypesIdUsagesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.usages = self._register_child_endpoint(CompanyContactTypesIdUsagesEndpoint(client, parent_endpoint=self))
