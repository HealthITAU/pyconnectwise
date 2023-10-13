from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdActivitiesEndpoint import ProjectTicketsIdActivitiesEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdAllnotesEndpoint import ProjectTicketsIdAllnotesEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdConfigurationsEndpoint import ProjectTicketsIdConfigurationsEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdConvertEndpoint import ProjectTicketsIdConvertEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdDocumentsEndpoint import ProjectTicketsIdDocumentsEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdNotesEndpoint import ProjectTicketsIdNotesEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdProductsEndpoint import ProjectTicketsIdProductsEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdScheduleentriesEndpoint import \
    ProjectTicketsIdScheduleentriesEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdTasksEndpoint import ProjectTicketsIdTasksEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketsIdTimeentriesEndpoint import ProjectTicketsIdTimeentriesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectTicket
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectTicketsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ProjectTicket, ConnectWiseManageRequestParams],
    IPuttable[ProjectTicket, ConnectWiseManageRequestParams],
    IPatchable[ProjectTicket, ConnectWiseManageRequestParams],
    IPaginateable[ProjectTicket, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ProjectTicket)
        IPuttable.__init__(self, ProjectTicket)
        IPatchable.__init__(self, ProjectTicket)
        IPaginateable.__init__(self, ProjectTicket)

        self.configurations = self._register_child_endpoint(
            ProjectTicketsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.documents = self._register_child_endpoint(ProjectTicketsIdDocumentsEndpoint(client, parent_endpoint=self))
        self.convert = self._register_child_endpoint(ProjectTicketsIdConvertEndpoint(client, parent_endpoint=self))
        self.timeentries = self._register_child_endpoint(
            ProjectTicketsIdTimeentriesEndpoint(client, parent_endpoint=self)
        )
        self.products = self._register_child_endpoint(ProjectTicketsIdProductsEndpoint(client, parent_endpoint=self))
        self.scheduleentries = self._register_child_endpoint(
            ProjectTicketsIdScheduleentriesEndpoint(client, parent_endpoint=self)
        )
        self.all_notes = self._register_child_endpoint(ProjectTicketsIdAllnotesEndpoint(client, parent_endpoint=self))
        self.notes = self._register_child_endpoint(ProjectTicketsIdNotesEndpoint(client, parent_endpoint=self))
        self.tasks = self._register_child_endpoint(ProjectTicketsIdTasksEndpoint(client, parent_endpoint=self))
        self.activities = self._register_child_endpoint(
            ProjectTicketsIdActivitiesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectTicket]:
        """
        Performs a GET request against the /project/tickets/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectTicket:
        """
        Performs a GET request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicket: The parsed response data.
        """
        return self._parse_one(ProjectTicket, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectTicket:
        """
        Performs a PUT request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicket: The parsed response data.
        """
        return self._parse_one(ProjectTicket, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> ProjectTicket:
        """
        Performs a PATCH request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicket: The parsed response data.
        """
        return self._parse_one(ProjectTicket, super()._make_request("PATCH", data=data, params=params).json())
