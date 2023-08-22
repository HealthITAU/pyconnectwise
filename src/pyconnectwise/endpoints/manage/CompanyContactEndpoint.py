from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesEndpoint import CompanyContactTypesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contact", parent_endpoint=parent_endpoint)

        self.types = self._register_child_endpoint(CompanyContactTypesEndpoint(client, parent_endpoint=self))
