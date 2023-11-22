from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesCountEndpoint import SystemSecurityrolesCountEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesIdEndpoint import SystemSecurityrolesIdEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesInfoEndpoint import SystemSecurityrolesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import SecurityRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemSecurityrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SecurityRole], ConnectWiseManageRequestParams],
    IPostable[SecurityRole, ConnectWiseManageRequestParams],
    IPaginateable[SecurityRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "securityroles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SecurityRole])
        IPostable.__init__(self, SecurityRole)
        IPaginateable.__init__(self, SecurityRole)

        self.count = self._register_child_endpoint(SystemSecurityrolesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemSecurityrolesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemSecurityrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSecurityrolesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemSecurityrolesIdEndpoint: The initialized SystemSecurityrolesIdEndpoint object.
        """
        child = SystemSecurityrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[SecurityRole]:
        """
        Performs a GET request against the /system/securityroles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SecurityRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), SecurityRole, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[SecurityRole]:
        """
        Performs a GET request against the /system/securityroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SecurityRole]: The parsed response data.
        """
        return self._parse_many(SecurityRole, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SecurityRole:
        """
        Performs a POST request against the /system/securityroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SecurityRole: The parsed response data.
        """
        return self._parse_one(SecurityRole, super()._make_request("POST", data=data, params=params).json())
