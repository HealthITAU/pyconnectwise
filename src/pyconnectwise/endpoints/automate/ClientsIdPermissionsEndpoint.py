from typing import Any

from pyconnectwise.endpoints.automate.ClientsIdPermissionsIdEndpoint import ClientsIdPermissionsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ClientsIdPermissionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Permissions", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ClientsIdPermissionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ClientsIdPermissionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ClientsIdPermissionsIdEndpoint: The initialized ClientsIdPermissionsIdEndpoint object.
        """
        child = ClientsIdPermissionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
