from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDocumenttypesIdEndpoint import SystemDocumenttypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemDocumenttypesInfoEndpoint import SystemDocumenttypesInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemDocumenttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documentTypes", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemDocumenttypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemDocumenttypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemDocumenttypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemDocumenttypesIdEndpoint: The initialized SystemDocumenttypesIdEndpoint object.
        """
        child = SystemDocumenttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
