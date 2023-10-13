from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServicePriorityIdEndpoint import ServicePriorityIdEndpoint
from pyconnectwise.endpoints.manage.ServicePriorityInfoEndpoint import ServicePriorityInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServicePriorityEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "priority", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ServicePriorityInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServicePriorityIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServicePriorityIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServicePriorityIdEndpoint: The initialized ServicePriorityIdEndpoint object.
        """
        child = ServicePriorityIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
