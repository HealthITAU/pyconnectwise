from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesServicePriorityInfoEndpoint import SalesServicePriorityInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesServicePriorityEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "priority", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesServicePriorityInfoEndpoint(client, parent_endpoint=self))
