from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import ProjectSecurityRoleSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProjectSecurityrolesIdSettingsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ProjectSecurityRoleSetting, ConnectWiseManageRequestParams],
    IPatchable[ProjectSecurityRoleSetting, ConnectWiseManageRequestParams],
    IPuttable[ProjectSecurityRoleSetting, ConnectWiseManageRequestParams],
    IPaginateable[ProjectSecurityRoleSetting, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ProjectSecurityRoleSetting)
        IPatchable.__init__(self, ProjectSecurityRoleSetting)
        IPuttable.__init__(self, ProjectSecurityRoleSetting)
        IPaginateable.__init__(self, ProjectSecurityRoleSetting)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectSecurityRoleSetting]:
        """
        Performs a GET request against the /project/securityRoles/{id}/settings/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectSecurityRoleSetting]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectSecurityRoleSetting, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectSecurityRoleSetting:
        """
        Performs a GET request against the /project/securityRoles/{id}/settings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectSecurityRoleSetting: The parsed response data.
        """
        return self._parse_one(
            ProjectSecurityRoleSetting, super()._make_request("GET", data=data, params=params).json()
        )

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectSecurityRoleSetting:
        """
        Performs a PATCH request against the /project/securityRoles/{id}/settings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectSecurityRoleSetting: The parsed response data.
        """
        return self._parse_one(
            ProjectSecurityRoleSetting, super()._make_request("PATCH", data=data, params=params).json()
        )

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectSecurityRoleSetting:
        """
        Performs a PUT request against the /project/securityRoles/{id}/settings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectSecurityRoleSetting: The parsed response data.
        """
        return self._parse_one(
            ProjectSecurityRoleSetting, super()._make_request("PUT", data=data, params=params).json()
        )
