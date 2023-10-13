from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesIdEndpoint import SystemSecurityrolesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemSecurityrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "securityRoles", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemSecurityrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSecurityrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSecurityrolesIdEndpoint: The initialized SystemSecurityrolesIdEndpoint object.
        """
        child = SystemSecurityrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
