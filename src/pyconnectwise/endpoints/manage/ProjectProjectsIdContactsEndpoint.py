from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdContactsIdEndpoint import ProjectProjectsIdContactsIdEndpoint
from pyconnectwise.models.manage import ProjectContact
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectProjectsIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectContact, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectContact]:
        """
        Performs a GET request against the /project/projects/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectContact]: The parsed response data.
        """
        return self._parse_many(ProjectContact, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectContact:
        """
        Performs a POST request against the /project/projects/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectContact: The parsed response data.
        """
        return self._parse_one(ProjectContact, super()._make_request("POST", data=data, params=params).json())
