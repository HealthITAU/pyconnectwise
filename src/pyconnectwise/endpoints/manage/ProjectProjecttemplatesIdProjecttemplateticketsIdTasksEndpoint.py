from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdProjecttemplateticketsIdTasksCountEndpoint import \
    ProjectProjecttemplatesIdProjecttemplateticketsIdTasksCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint import \
    ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectTemplateTask
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectProjecttemplatesIdProjecttemplateticketsIdTasksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectTemplateTask], ConnectWiseManageRequestParams],
    IPostable[ProjectTemplateTask, ConnectWiseManageRequestParams],
    IPaginateable[ProjectTemplateTask, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "tasks", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectTemplateTask])
        IPostable.__init__(self, ProjectTemplateTask)
        IPaginateable.__init__(self, ProjectTemplateTask)

        self.count = self._register_child_endpoint(
            ProjectProjecttemplatesIdProjecttemplateticketsIdTasksCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint: The initialized ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint object.
        """
        child = ProjectProjecttemplatesIdProjecttemplateticketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectTemplateTask]:
        """
        Performs a GET request against the /project/projectTemplates/{id}/projectTemplateTickets/{id}/tasks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTemplateTask]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectTemplateTask, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectTemplateTask]:
        """
        Performs a GET request against the /project/projectTemplates/{id}/projectTemplateTickets/{id}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTemplateTask]: The parsed response data.
        """
        return self._parse_many(ProjectTemplateTask, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectTemplateTask:
        """
        Performs a POST request against the /project/projectTemplates/{id}/projectTemplateTickets/{id}/tasks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTemplateTask: The parsed response data.
        """
        return self._parse_one(ProjectTemplateTask, super()._make_request("POST", data=data, params=params).json())
