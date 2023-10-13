from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembertemplatesCountEndpoint import SystemMembertemplatesCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembertemplatesIdEndpoint import SystemMembertemplatesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMembertemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "membertemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMembertemplatesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMembertemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembertemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembertemplatesIdEndpoint: The initialized SystemMembertemplatesIdEndpoint object.
        """
        child = SystemMembertemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
