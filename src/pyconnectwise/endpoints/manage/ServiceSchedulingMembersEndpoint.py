from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSchedulingMembersIdEndpoint import ServiceSchedulingMembersIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSchedulingMembersInfoEndpoint import ServiceSchedulingMembersInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceSchedulingMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "members", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ServiceSchedulingMembersInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSchedulingMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSchedulingMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSchedulingMembersIdEndpoint: The initialized ServiceSchedulingMembersIdEndpoint object.
        """
        child = ServiceSchedulingMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
