from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsopenedCountEndpoint import (
    MarketingCampaignsIdEmailsopenedCountEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsopenedIdEndpoint import (
    MarketingCampaignsIdEmailsopenedIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import EmailOpened
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class MarketingCampaignsIdEmailsopenedEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[EmailOpened], ConnectWiseManageRequestParams],
    IPostable[EmailOpened, ConnectWiseManageRequestParams],
    IPaginateable[EmailOpened, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "emailsOpened", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[EmailOpened])
        IPostable.__init__(self, EmailOpened)
        IPaginateable.__init__(self, EmailOpened)

        self.count = self._register_child_endpoint(
            MarketingCampaignsIdEmailsopenedCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsIdEmailsopenedIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdEmailsopenedIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsIdEmailsopenedIdEndpoint: The initialized MarketingCampaignsIdEmailsopenedIdEndpoint object.
        """
        child = MarketingCampaignsIdEmailsopenedIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[EmailOpened]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/emailsOpened endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailOpened]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            EmailOpened,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[EmailOpened]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/emailsOpened endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailOpened]: The parsed response data.
        """
        return self._parse_many(
            EmailOpened, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> EmailOpened:
        """
        Performs a POST request against the /marketing/campaigns/{id}/emailsOpened endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailOpened: The parsed response data.
        """
        return self._parse_one(
            EmailOpened, super()._make_request("POST", data=data, params=params).json()
        )
