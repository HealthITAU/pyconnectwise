from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsCountEndpoint import ProjectTicketsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdEndpoint import ProjectTicketsIdEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsSearchEndpoint import ProjectTicketsSearchEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectTicket
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectTicketsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectTicket], ConnectWiseManageRequestParams],
    IPostable[ProjectTicket, ConnectWiseManageRequestParams],
    IPaginateable[ProjectTicket, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "tickets", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectTicket])
        IPostable.__init__(self, ProjectTicket)
        IPaginateable.__init__(self, ProjectTicket)

        self.count = self._register_child_endpoint(ProjectTicketsCountEndpoint(client, parent_endpoint=self))
        self.search = self._register_child_endpoint(ProjectTicketsSearchEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectTicketsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectTicketsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectTicketsIdEndpoint: The initialized ProjectTicketsIdEndpoint object.
        """
        child = ProjectTicketsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectTicket]:
        """
        Performs a GET request against the /project/tickets endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTicket]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectTicket, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectTicket]:
        """
        Performs a GET request against the /project/tickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTicket]: The parsed response data.
        """
        return self._parse_many(ProjectTicket, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectTicket:
        """
        Performs a POST request against the /project/tickets endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicket: The parsed response data.
        """
        return self._parse_one(ProjectTicket, super()._make_request("POST", data=data, params=params).json())
