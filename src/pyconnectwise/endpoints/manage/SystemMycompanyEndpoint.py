from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyDocumentsEndpoint import SystemMycompanyDocumentsEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyInfoEndpoint import SystemMycompanyInfoEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyReportingservicesEndpoint import \
    SystemMycompanyReportingservicesEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyServicesEndpoint import SystemMycompanyServicesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "mycompany", parent_endpoint=parent_endpoint)

        self.reporting_services = self._register_child_endpoint(
            SystemMycompanyReportingservicesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(SystemMycompanyInfoEndpoint(client, parent_endpoint=self))
        self.services = self._register_child_endpoint(SystemMycompanyServicesEndpoint(client, parent_endpoint=self))
        self.documents = self._register_child_endpoint(SystemMycompanyDocumentsEndpoint(client, parent_endpoint=self))
