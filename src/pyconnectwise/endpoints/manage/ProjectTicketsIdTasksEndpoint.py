from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdTasksCountEndpoint import (
    ProjectTicketsIdTasksCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProjectTicketsIdTasksIdEndpoint import (
    ProjectTicketsIdTasksIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import TicketTask
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProjectTicketsIdTasksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TicketTask], ConnectWiseManageRequestParams],
    IPostable[TicketTask, ConnectWiseManageRequestParams],
    IPaginateable[TicketTask, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "tasks", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TicketTask])
        IPostable.__init__(self, TicketTask)
        IPaginateable.__init__(self, TicketTask)

        self.count = self._register_child_endpoint(
            ProjectTicketsIdTasksCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectTicketsIdTasksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectTicketsIdTasksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectTicketsIdTasksIdEndpoint: The initialized ProjectTicketsIdTasksIdEndpoint object.
        """
        child = ProjectTicketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TicketTask]:
        """
        Performs a GET request against the /project/tickets/{id}/tasks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TicketTask]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TicketTask,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TicketTask]:
        """
        Performs a GET request against the /project/tickets/{id}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TicketTask]: The parsed response data.
        """
        return self._parse_many(
            TicketTask, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TicketTask:
        """
        Performs a POST request against the /project/tickets/{id}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketTask: The parsed response data.
        """
        return self._parse_one(
            TicketTask, super()._make_request("POST", data=data, params=params).json()
        )
