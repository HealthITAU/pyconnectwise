from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesRolesCountEndpoint import SalesRolesCountEndpoint
from pyconnectwise.endpoints.manage.SalesRolesIdEndpoint import SalesRolesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Role
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesRolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Role], ConnectWiseManageRequestParams],
    IPostable[Role, ConnectWiseManageRequestParams],
    IPaginateable[Role, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "roles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Role])
        IPostable.__init__(self, Role)
        IPaginateable.__init__(self, Role)

        self.count = self._register_child_endpoint(SalesRolesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesRolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesRolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesRolesIdEndpoint: The initialized SalesRolesIdEndpoint object.
        """
        child = SalesRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Role]:
        """
        Performs a GET request against the /sales/roles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Role]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Role, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Role]:
        """
        Performs a GET request against the /sales/roles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Role]: The parsed response data.
        """
        return self._parse_many(Role, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Role:
        """
        Performs a POST request against the /sales/roles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Role: The parsed response data.
        """
        return self._parse_one(Role, super()._make_request("POST", data=data, params=params).json())
