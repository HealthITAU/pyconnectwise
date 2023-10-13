from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesCountEndpoint import ProjectProjecttemplatesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdEndpoint import ProjectProjecttemplatesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectProjecttemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "projectTemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectProjecttemplatesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectProjecttemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjecttemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjecttemplatesIdEndpoint: The initialized ProjectProjecttemplatesIdEndpoint object.
        """
        child = ProjectProjecttemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
