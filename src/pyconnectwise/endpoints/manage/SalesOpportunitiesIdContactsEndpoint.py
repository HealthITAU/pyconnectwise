from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsCountEndpoint import (
    SalesOpportunitiesIdContactsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsIdEndpoint import SalesOpportunitiesIdContactsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import OpportunityContact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesOpportunitiesIdContactsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[OpportunityContact], ConnectWiseManageRequestParams],
    IPostable[OpportunityContact, ConnectWiseManageRequestParams],
    IPaginateable[OpportunityContact, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "contacts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[OpportunityContact])
        IPostable.__init__(self, OpportunityContact)
        IPaginateable.__init__(self, OpportunityContact)

        self.count = self._register_child_endpoint(
            SalesOpportunitiesIdContactsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> SalesOpportunitiesIdContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdContactsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdContactsIdEndpoint: The initialized SalesOpportunitiesIdContactsIdEndpoint object.
        """
        child = SalesOpportunitiesIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[OpportunityContact]:
        """
        Performs a GET request against the /sales/opportunities/{id}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityContact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityContact, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[OpportunityContact]:
        """
        Performs a GET request against the /sales/opportunities/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityContact]: The parsed response data.
        """
        return self._parse_many(OpportunityContact, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> OpportunityContact:
        """
        Performs a POST request against the /sales/opportunities/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityContact: The parsed response data.
        """
        return self._parse_one(OpportunityContact, super()._make_request("POST", data=data, params=params).json())
