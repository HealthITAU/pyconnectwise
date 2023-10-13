from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceClosedinvoicesIdEndpoint import FinanceClosedinvoicesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceClosedinvoicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "closedInvoices", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> FinanceClosedinvoicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceClosedinvoicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceClosedinvoicesIdEndpoint: The initialized FinanceClosedinvoicesIdEndpoint object.
        """
        child = FinanceClosedinvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
