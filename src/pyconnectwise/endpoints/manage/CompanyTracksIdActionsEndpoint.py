from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyTracksIdActionsIdEndpoint import CompanyTracksIdActionsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdActionsCountEndpoint import CompanyTracksIdActionsCountEndpoint
from pyconnectwise.models.manage.TrackActionModel import TrackActionModel

class CompanyTracksIdActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "actions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyTracksIdActionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TrackActionModel]:
        """
        Performs a GET request against the /company/tracks/{parentId}/actions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TrackActionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TrackActionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TrackActionModel]:
        """
        Performs a GET request against the /company/tracks/{parentId}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TrackActionModel]: The parsed response data.
        """
        return self._parse_many(TrackActionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TrackActionModel:
        """
        Performs a POST request against the /company/tracks/{parentId}/actions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TrackActionModel: The parsed response data.
        """
        return self._parse_one(TrackActionModel, super().make_request("POST", params=params).json())
        