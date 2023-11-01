from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemGoogleemailsetupCountEndpoint import (
    SystemGoogleemailsetupCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemGoogleemailsetupIdEndpoint import (
    SystemGoogleemailsetupIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemGoogleemailsetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "googleemailsetup", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            SystemGoogleemailsetupCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemGoogleemailsetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemGoogleemailsetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemGoogleemailsetupIdEndpoint: The initialized SystemGoogleemailsetupIdEndpoint object.
        """
        child = SystemGoogleemailsetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
