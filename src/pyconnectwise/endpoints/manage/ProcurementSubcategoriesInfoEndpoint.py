from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesInfoCountEndpoint import \
    ProcurementSubcategoriesInfoCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementSubcategoriesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementSubcategoriesInfoCountEndpoint(client, parent_endpoint=self)
        )
