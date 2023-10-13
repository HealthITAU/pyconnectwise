from typing import Any

from pyconnectwise.endpoints.automate.ExternalsystemcredentialsClientsIdEndpoint import \
    ExternalsystemcredentialsClientsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ExternalsystemcredentialsClientsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Clients", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ExternalsystemcredentialsClientsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExternalsystemcredentialsClientsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExternalsystemcredentialsClientsIdEndpoint: The initialized ExternalsystemcredentialsClientsIdEndpoint object.
        """
        child = ExternalsystemcredentialsClientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
