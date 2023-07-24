from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoTypesEndpoint import CompanyCompaniesInfoTypesEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.types = self._register_child_endpoint(CompanyCompaniesInfoTypesEndpoint(client, parent_endpoint=self))
