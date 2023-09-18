from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityrolesIdSettingsCountEndpoint import \
    ProjectSecurityrolesIdSettingsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityrolesIdSettingsIdEndpoint import \
    ProjectSecurityrolesIdSettingsIdEndpoint
from pyconnectwise.models.manage import ProjectSecurityRoleSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectSecurityrolesIdSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProjectSecurityrolesIdSettingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectSecurityrolesIdSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectSecurityrolesIdSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectSecurityrolesIdSettingsIdEndpoint: The initialized ProjectSecurityrolesIdSettingsIdEndpoint object.
        """
        child = ProjectSecurityrolesIdSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectSecurityRoleSetting]:
        """
        Performs a GET request against the /project/securityRoles/{id}/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectSecurityRoleSetting]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectSecurityRoleSetting, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectSecurityRoleSetting]:
        """
        Performs a GET request against the /project/securityRoles/{id}/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectSecurityRoleSetting]: The parsed response data.
        """
        return self._parse_many(
            ProjectSecurityRoleSetting, super()._make_request("GET", data=data, params=params).json()
        )
