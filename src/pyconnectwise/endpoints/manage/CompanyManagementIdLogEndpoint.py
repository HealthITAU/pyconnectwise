from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdLogDownloadEndpoint import CompanyManagementIdLogDownloadEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManagementIdLogEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "log", parent_endpoint=parent_endpoint)

        self.download = self._register_child_endpoint(
            CompanyManagementIdLogDownloadEndpoint(client, parent_endpoint=self)
        )
