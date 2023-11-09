from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsTabletypesCountEndpoint import SystemWorkflowsTabletypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsTabletypesIdEndpoint import SystemWorkflowsTabletypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsTabletypesInfoEndpoint import SystemWorkflowsTabletypesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import WorkflowTableType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowsTabletypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowTableType], ConnectWiseManageRequestParams],
    IPaginateable[WorkflowTableType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "tableTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[WorkflowTableType])
        IPaginateable.__init__(self, WorkflowTableType)

        self.count = self._register_child_endpoint(SystemWorkflowsTabletypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemWorkflowsTabletypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemWorkflowsTabletypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsTabletypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemWorkflowsTabletypesIdEndpoint: The initialized SystemWorkflowsTabletypesIdEndpoint object.
        """
        child = SystemWorkflowsTabletypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkflowTableType]:
        """
        Performs a GET request against the /system/workflows/tableTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowTableType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowTableType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[WorkflowTableType]:
        """
        Performs a GET request against the /system/workflows/tableTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTableType]: The parsed response data.
        """
        return self._parse_many(WorkflowTableType, super()._make_request("GET", data=data, params=params).json())
