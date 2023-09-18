from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdActivitiesEndpoint import MarketingCampaignsIdActivitiesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsEndpoint import MarketingCampaignsIdAuditsEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsopenedEndpoint import \
    MarketingCampaignsIdEmailsopenedEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdFormssubmittedEndpoint import \
    MarketingCampaignsIdFormssubmittedEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdLinksclickedEndpoint import \
    MarketingCampaignsIdLinksclickedEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdOpportunitiesEndpoint import \
    MarketingCampaignsIdOpportunitiesEndpoint
from pyconnectwise.models.manage import Campaign
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.links_clicked = self._register_child_endpoint(
            MarketingCampaignsIdLinksclickedEndpoint(client, parent_endpoint=self)
        )
        self.audits = self._register_child_endpoint(MarketingCampaignsIdAuditsEndpoint(client, parent_endpoint=self))
        self.opportunities = self._register_child_endpoint(
            MarketingCampaignsIdOpportunitiesEndpoint(client, parent_endpoint=self)
        )
        self.activities = self._register_child_endpoint(
            MarketingCampaignsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.forms_submitted = self._register_child_endpoint(
            MarketingCampaignsIdFormssubmittedEndpoint(client, parent_endpoint=self)
        )
        self.emails_opened = self._register_child_endpoint(
            MarketingCampaignsIdEmailsopenedEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Campaign]:
        """
        Performs a GET request against the /marketing/campaigns/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Campaign]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Campaign, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Campaign:
        """
        Performs a GET request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Campaign:
        """
        Performs a PUT request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Campaign:
        """
        Performs a PATCH request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("PATCH", data=data, params=params).json())
