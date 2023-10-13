from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesIdEndpoint import CompanyContactTypesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyContactTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> CompanyContactTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactTypesIdEndpoint: The initialized CompanyContactTypesIdEndpoint object.
        """
        child = CompanyContactTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
