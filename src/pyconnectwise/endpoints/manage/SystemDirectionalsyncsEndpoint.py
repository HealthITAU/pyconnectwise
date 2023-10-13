from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDirectionalsyncsIdEndpoint import SystemDirectionalsyncsIdEndpoint
from pyconnectwise.endpoints.manage.SystemDirectionalsyncsInfoEndpoint import SystemDirectionalsyncsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemDirectionalsyncsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "directionalSyncs", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemDirectionalsyncsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemDirectionalsyncsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemDirectionalsyncsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemDirectionalsyncsIdEndpoint: The initialized SystemDirectionalsyncsIdEndpoint object.
        """
        child = SystemDirectionalsyncsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
