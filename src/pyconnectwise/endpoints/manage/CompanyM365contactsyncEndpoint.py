from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncIdEndpoint import CompanyM365contactsyncIdEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncPropertyEndpoint import CompanyM365contactsyncPropertyEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyM365contactsyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "m365contactsync", parent_endpoint=parent_endpoint)

        self.property = self._register_child_endpoint(
            CompanyM365contactsyncPropertyEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyM365contactsyncIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyM365contactsyncIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyM365contactsyncIdEndpoint: The initialized CompanyM365contactsyncIdEndpoint object.
        """
        child = CompanyM365contactsyncIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
