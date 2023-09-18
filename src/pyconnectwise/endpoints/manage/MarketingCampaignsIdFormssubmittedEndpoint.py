from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdFormssubmittedCountEndpoint import \
    MarketingCampaignsIdFormssubmittedCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdFormssubmittedIdEndpoint import \
    MarketingCampaignsIdFormssubmittedIdEndpoint
from pyconnectwise.models.manage import FormSubmitted
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsIdFormssubmittedEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "formsSubmitted", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingCampaignsIdFormssubmittedCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsIdFormssubmittedIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdFormssubmittedIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsIdFormssubmittedIdEndpoint: The initialized MarketingCampaignsIdFormssubmittedIdEndpoint object.
        """
        child = MarketingCampaignsIdFormssubmittedIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[FormSubmitted]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/formsSubmitted endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[FormSubmitted]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), FormSubmitted, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[FormSubmitted]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/formsSubmitted endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[FormSubmitted]: The parsed response data.
        """
        return self._parse_many(FormSubmitted, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> FormSubmitted:
        """
        Performs a POST request against the /marketing/campaigns/{id}/formsSubmitted endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            FormSubmitted: The parsed response data.
        """
        return self._parse_one(FormSubmitted, super()._make_request("POST", data=data, params=params).json())
