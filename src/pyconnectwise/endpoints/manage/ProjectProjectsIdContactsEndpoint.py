from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdContactsIdEndpoint import (
    ProjectProjectsIdContactsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ProjectContact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProjectProjectsIdContactsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectContact], ConnectWiseManageRequestParams],
    IPostable[ProjectContact, ConnectWiseManageRequestParams],
    IPaginateable[ProjectContact, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "contacts", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ProjectContact])
        IPostable.__init__(self, ProjectContact)
        IPaginateable.__init__(self, ProjectContact)

    def id(self, id: int) -> ProjectProjectsIdContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdContactsIdEndpoint: The initialized ProjectProjectsIdContactsIdEndpoint object.
        """
        child = ProjectProjectsIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ProjectContact]:
        """
        Performs a GET request against the /project/projects/{id}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectContact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProjectContact,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ProjectContact]:
        """
        Performs a GET request against the /project/projects/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectContact]: The parsed response data.
        """
        return self._parse_many(
            ProjectContact,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProjectContact:
        """
        Performs a POST request against the /project/projects/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectContact: The parsed response data.
        """
        return self._parse_one(
            ProjectContact,
            super()._make_request("POST", data=data, params=params).json(),
        )
