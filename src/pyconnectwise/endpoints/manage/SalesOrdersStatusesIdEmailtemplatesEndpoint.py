from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEmailtemplatesCountEndpoint import \
    SalesOrdersStatusesIdEmailtemplatesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEmailtemplatesIdEndpoint import \
    SalesOrdersStatusesIdEmailtemplatesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesOrdersStatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "emailtemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SalesOrdersStatusesIdEmailtemplatesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOrdersStatusesIdEmailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOrdersStatusesIdEmailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOrdersStatusesIdEmailtemplatesIdEndpoint: The initialized SalesOrdersStatusesIdEmailtemplatesIdEndpoint object.
        """
        child = SalesOrdersStatusesIdEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
