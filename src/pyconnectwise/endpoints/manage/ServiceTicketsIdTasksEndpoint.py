from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksCountEndpoint import ServiceTicketsIdTasksCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksIdEndpoint import ServiceTicketsIdTasksIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Task
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceTicketsIdTasksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Task], ConnectWiseManageRequestParams],
    IPostable[Task, ConnectWiseManageRequestParams],
    IPaginateable[Task, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "tasks", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Task])
        IPostable.__init__(self, Task)
        IPaginateable.__init__(self, Task)

        self.count = self._register_child_endpoint(ServiceTicketsIdTasksCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceTicketsIdTasksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsIdTasksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsIdTasksIdEndpoint: The initialized ServiceTicketsIdTasksIdEndpoint object.
        """
        child = ServiceTicketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Task]:
        """
        Performs a GET request against the /service/tickets/{id}/tasks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Task]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Task, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Task]:
        """
        Performs a GET request against the /service/tickets/{id}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Task]: The parsed response data.
        """
        return self._parse_many(Task, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Task:
        """
        Performs a POST request against the /service/tickets/{id}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Task: The parsed response data.
        """
        return self._parse_one(Task, super()._make_request("POST", data=data, params=params).json())
