from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdProjecttemplateticketsCountEndpoint import \
    ProjectProjecttemplatesIdProjecttemplateticketsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint import \
    ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectTemplateTicket
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectProjecttemplatesIdProjecttemplateticketsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectTemplateTicket], ConnectWiseManageRequestParams],
    IPostable[ProjectTemplateTicket, ConnectWiseManageRequestParams],
    IPaginateable[ProjectTemplateTicket, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "projectTemplateTickets", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectTemplateTicket])
        IPostable.__init__(self, ProjectTemplateTicket)
        IPaginateable.__init__(self, ProjectTemplateTicket)

        self.count = self._register_child_endpoint(
            ProjectProjecttemplatesIdProjecttemplateticketsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint: The initialized ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint object.
        """
        child = ProjectProjecttemplatesIdProjecttemplateticketsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectTemplateTicket]:
        """
        Performs a GET request against the /project/projectTemplates/{id}/projectTemplateTickets endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTemplateTicket]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectTemplateTicket, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectTemplateTicket]:
        """
        Performs a GET request against the /project/projectTemplates/{id}/projectTemplateTickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTemplateTicket]: The parsed response data.
        """
        return self._parse_many(ProjectTemplateTicket, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectTemplateTicket:
        """
        Performs a POST request against the /project/projectTemplates/{id}/projectTemplateTickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTemplateTicket: The parsed response data.
        """
        return self._parse_one(ProjectTemplateTicket, super()._make_request("POST", data=data, params=params).json())
