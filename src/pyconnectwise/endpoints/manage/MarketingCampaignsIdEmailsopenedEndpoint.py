from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsopenedCountEndpoint import \
    MarketingCampaignsIdEmailsopenedCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsopenedIdEndpoint import \
    MarketingCampaignsIdEmailsopenedIdEndpoint
from pyconnectwise.models.manage import EmailOpened
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsIdEmailsopenedEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailsOpened", parent_endpoint=parent_endpoint)

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
        child = MarketingCampaignsIdEmailsopenedIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[EmailOpened]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/emailsOpened endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailOpened]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), EmailOpened, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EmailOpened]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/emailsOpened endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailOpened]: The parsed response data.
        """
        return self._parse_many(EmailOpened, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailOpened:
        """
        Performs a POST request against the /marketing/campaigns/{id}/emailsOpened endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailOpened: The parsed response data.
        """
        return self._parse_one(EmailOpened, super()._make_request("POST", data=data, params=params).json())
