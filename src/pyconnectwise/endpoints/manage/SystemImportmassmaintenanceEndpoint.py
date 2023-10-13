from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemImportmassmaintenanceIdEndpoint import SystemImportmassmaintenanceIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemImportmassmaintenanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "importMassMaintenance", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemImportmassmaintenanceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemImportmassmaintenanceIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemImportmassmaintenanceIdEndpoint: The initialized SystemImportmassmaintenanceIdEndpoint object.
        """
        child = SystemImportmassmaintenanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
