from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsCountEndpoint import MarketingGroupsIdContactsCountEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsIdEndpoint import MarketingGroupsIdContactsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import MarketingContact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class MarketingGroupsIdContactsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MarketingContact], ConnectWiseManageRequestParams],
    IPostable[MarketingContact, ConnectWiseManageRequestParams],
    IPaginateable[MarketingContact, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "contacts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[MarketingContact])
        IPostable.__init__(self, MarketingContact)
        IPaginateable.__init__(self, MarketingContact)

        self.count = self._register_child_endpoint(MarketingGroupsIdContactsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> MarketingGroupsIdContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingGroupsIdContactsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            MarketingGroupsIdContactsIdEndpoint: The initialized MarketingGroupsIdContactsIdEndpoint object.
        """
        child = MarketingGroupsIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[MarketingContact]:
        """
        Performs a GET request against the /marketing/groups/{id}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MarketingContact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), MarketingContact, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[MarketingContact]:
        """
        Performs a GET request against the /marketing/groups/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MarketingContact]: The parsed response data.
        """
        return self._parse_many(MarketingContact, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> MarketingContact:
        """
        Performs a POST request against the /marketing/groups/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketingContact: The parsed response data.
        """
        return self._parse_one(MarketingContact, super()._make_request("POST", data=data, params=params).json())
