from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesCountEndpoint import SalesOpportunitiesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesDefaultEndpoint import SalesOpportunitiesDefaultEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdEndpoint import SalesOpportunitiesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsEndpoint import SalesOpportunitiesRatingsEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesEndpoint import SalesOpportunitiesStatusesEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesEndpoint import SalesOpportunitiesTypesEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Opportunity
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesOpportunitiesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Opportunity], ConnectWiseManageRequestParams],
    IPostable[Opportunity, ConnectWiseManageRequestParams],
    IPaginateable[Opportunity, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "opportunities", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Opportunity])
        IPostable.__init__(self, Opportunity)
        IPaginateable.__init__(self, Opportunity)

        self.count = self._register_child_endpoint(SalesOpportunitiesCountEndpoint(client, parent_endpoint=self))
        self.default = self._register_child_endpoint(SalesOpportunitiesDefaultEndpoint(client, parent_endpoint=self))
        self.ratings = self._register_child_endpoint(SalesOpportunitiesRatingsEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(SalesOpportunitiesStatusesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(SalesOpportunitiesTypesEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SalesOpportunitiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdEndpoint: The initialized SalesOpportunitiesIdEndpoint object.
        """
        child = SalesOpportunitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Opportunity]:
        """
        Performs a GET request against the /sales/opportunities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Opportunity]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), Opportunity, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Opportunity]:
        """
        Performs a GET request against the /sales/opportunities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Opportunity]: The parsed response data.
        """
        return self._parse_many(Opportunity, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Opportunity:
        """
        Performs a POST request against the /sales/opportunities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Opportunity: The parsed response data.
        """
        return self._parse_one(Opportunity, super()._make_request("POST", data=data, params=params).json())
