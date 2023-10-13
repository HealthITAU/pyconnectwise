from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsyncCompanysyncIdEndpoint import \
    CompanyContactsyncCompanysyncIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyContactsyncCompanysyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "companysync", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> CompanyContactsyncCompanysyncIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsyncCompanysyncIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsyncCompanysyncIdEndpoint: The initialized CompanyContactsyncCompanysyncIdEndpoint object.
        """
        child = CompanyContactsyncCompanysyncIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
