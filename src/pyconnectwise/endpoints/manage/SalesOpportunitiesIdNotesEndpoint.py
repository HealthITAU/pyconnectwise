from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdNotesCountEndpoint import SalesOpportunitiesIdNotesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdNotesIdEndpoint import SalesOpportunitiesIdNotesIdEndpoint
from pyconnectwise.models.manage import OpportunityNote
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesOpportunitiesIdNotesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOpportunitiesIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdNotesIdEndpoint: The initialized SalesOpportunitiesIdNotesIdEndpoint object.
        """
        child = SalesOpportunitiesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityNote]:
        """
        Performs a GET request against the /sales/opportunities/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityNote]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityNote, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityNote]:
        """
        Performs a GET request against the /sales/opportunities/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityNote]: The parsed response data.
        """
        return self._parse_many(OpportunityNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityNote:
        """
        Performs a POST request against the /sales/opportunities/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityNote: The parsed response data.
        """
        return self._parse_one(OpportunityNote, super()._make_request("POST", data=data, params=params).json())
