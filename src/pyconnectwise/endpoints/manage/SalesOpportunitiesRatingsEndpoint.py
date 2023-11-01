from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsCountEndpoint import (
    SalesOpportunitiesRatingsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsIdEndpoint import (
    SalesOpportunitiesRatingsIdEndpoint,
)
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsInfoEndpoint import (
    SalesOpportunitiesRatingsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import OpportunityRating
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SalesOpportunitiesRatingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[OpportunityRating], ConnectWiseManageRequestParams],
    IPostable[OpportunityRating, ConnectWiseManageRequestParams],
    IPaginateable[OpportunityRating, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "ratings", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[OpportunityRating])
        IPostable.__init__(self, OpportunityRating)
        IPaginateable.__init__(self, OpportunityRating)

        self.count = self._register_child_endpoint(
            SalesOpportunitiesRatingsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SalesOpportunitiesRatingsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOpportunitiesRatingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesRatingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesRatingsIdEndpoint: The initialized SalesOpportunitiesRatingsIdEndpoint object.
        """
        child = SalesOpportunitiesRatingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[OpportunityRating]:
        """
        Performs a GET request against the /sales/opportunities/ratings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityRating]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OpportunityRating,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[OpportunityRating]:
        """
        Performs a GET request against the /sales/opportunities/ratings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityRating]: The parsed response data.
        """
        return self._parse_many(
            OpportunityRating,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> OpportunityRating:
        """
        Performs a POST request against the /sales/opportunities/ratings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityRating: The parsed response data.
        """
        return self._parse_one(
            OpportunityRating,
            super()._make_request("POST", data=data, params=params).json(),
        )
