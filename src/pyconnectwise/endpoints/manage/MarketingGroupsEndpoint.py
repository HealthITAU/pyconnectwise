from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsCountEndpoint import MarketingGroupsCountEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdEndpoint import MarketingGroupsIdEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsInfoEndpoint import MarketingGroupsInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Group
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class MarketingGroupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Group], ConnectWiseManageRequestParams],
    IPostable[Group, ConnectWiseManageRequestParams],
    IPaginateable[Group, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "groups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Group])
        IPostable.__init__(self, Group)
        IPaginateable.__init__(self, Group)

        self.count = self._register_child_endpoint(MarketingGroupsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(MarketingGroupsInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> MarketingGroupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingGroupsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            MarketingGroupsIdEndpoint: The initialized MarketingGroupsIdEndpoint object.
        """
        child = MarketingGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Group]:
        """
        Performs a GET request against the /marketing/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Group]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Group, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Group]:
        """
        Performs a GET request against the /marketing/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Group]: The parsed response data.
        """
        return self._parse_many(Group, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Group:
        """
        Performs a POST request against the /marketing/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(Group, super()._make_request("POST", data=data, params=params).json())
