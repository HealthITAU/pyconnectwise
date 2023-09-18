from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesCountEndpoint import \
    SalesOpportunitiesStatusesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesIdEndpoint import SalesOpportunitiesStatusesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesInfoEndpoint import SalesOpportunitiesStatusesInfoEndpoint
from pyconnectwise.models.manage import OpportunityStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SalesOpportunitiesStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(SalesOpportunitiesStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOpportunitiesStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesStatusesIdEndpoint: The initialized SalesOpportunitiesStatusesIdEndpoint object.
        """
        child = SalesOpportunitiesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityStatus]:
        """
        Performs a GET request against the /sales/opportunities/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityStatus]:
        """
        Performs a GET request against the /sales/opportunities/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityStatus]: The parsed response data.
        """
        return self._parse_many(OpportunityStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityStatus:
        """
        Performs a POST request against the /sales/opportunities/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStatus: The parsed response data.
        """
        return self._parse_one(OpportunityStatus, super()._make_request("POST", data=data, params=params).json())
