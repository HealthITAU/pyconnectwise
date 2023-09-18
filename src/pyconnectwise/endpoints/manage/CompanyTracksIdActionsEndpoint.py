from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdActionsCountEndpoint import CompanyTracksIdActionsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdActionsIdEndpoint import CompanyTracksIdActionsIdEndpoint
from pyconnectwise.models.manage import TrackAction
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyTracksIdActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "actions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyTracksIdActionsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyTracksIdActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyTracksIdActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyTracksIdActionsIdEndpoint: The initialized CompanyTracksIdActionsIdEndpoint object.
        """
        child = CompanyTracksIdActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TrackAction]:
        """
        Performs a GET request against the /company/tracks/{id}/actions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TrackAction]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TrackAction, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TrackAction]:
        """
        Performs a GET request against the /company/tracks/{id}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TrackAction]: The parsed response data.
        """
        return self._parse_many(TrackAction, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TrackAction:
        """
        Performs a POST request against the /company/tracks/{id}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TrackAction: The parsed response data.
        """
        return self._parse_one(TrackAction, super()._make_request("POST", data=data, params=params).json())
