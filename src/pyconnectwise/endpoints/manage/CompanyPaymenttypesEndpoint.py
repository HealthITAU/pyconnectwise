from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPaymenttypesInfoEndpoint import CompanyPaymenttypesInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPaymenttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentTypes", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyPaymenttypesInfoEndpoint(client, parent_endpoint=self))
