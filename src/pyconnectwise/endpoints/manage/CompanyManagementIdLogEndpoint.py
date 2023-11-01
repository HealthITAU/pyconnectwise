from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdLogDownloadEndpoint import (
    CompanyManagementIdLogDownloadEndpoint,
)


class CompanyManagementIdLogEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "log", parent_endpoint=parent_endpoint
        )

        self.download = self._register_child_endpoint(
            CompanyManagementIdLogDownloadEndpoint(client, parent_endpoint=self)
        )
