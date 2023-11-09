from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdActivitiesEndpoint import MarketingCampaignsIdActivitiesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsEndpoint import MarketingCampaignsIdAuditsEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsopenedEndpoint import (
    MarketingCampaignsIdEmailsopenedEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsIdFormssubmittedEndpoint import (
    MarketingCampaignsIdFormssubmittedEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsIdLinksclickedEndpoint import (
    MarketingCampaignsIdLinksclickedEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsIdOpportunitiesEndpoint import (
    MarketingCampaignsIdOpportunitiesEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import Campaign
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class MarketingCampaignsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Campaign, ConnectWiseManageRequestParams],
    IPatchable[Campaign, ConnectWiseManageRequestParams],
    IPuttable[Campaign, ConnectWiseManageRequestParams],
    IPaginateable[Campaign, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Campaign)
        IPatchable.__init__(self, Campaign)
        IPuttable.__init__(self, Campaign)
        IPaginateable.__init__(self, Campaign)

        self.forms_submitted = self._register_child_endpoint(
            MarketingCampaignsIdFormssubmittedEndpoint(client, parent_endpoint=self)
        )
        self.audits = self._register_child_endpoint(MarketingCampaignsIdAuditsEndpoint(client, parent_endpoint=self))
        self.emails_opened = self._register_child_endpoint(
            MarketingCampaignsIdEmailsopenedEndpoint(client, parent_endpoint=self)
        )
        self.activities = self._register_child_endpoint(
            MarketingCampaignsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.links_clicked = self._register_child_endpoint(
            MarketingCampaignsIdLinksclickedEndpoint(client, parent_endpoint=self)
        )
        self.opportunities = self._register_child_endpoint(
            MarketingCampaignsIdOpportunitiesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Campaign]:
        """
        Performs a GET request against the /marketing/campaigns/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Campaign]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Campaign, self, page, page_size, params)

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Campaign:
        """
        Performs a GET request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Campaign:
        """
        Performs a PATCH request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Campaign:
        """
        Performs a PUT request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("PUT", data=data, params=params).json())
