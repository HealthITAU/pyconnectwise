from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTracksIdEndpoint import CompanyCompaniesIdTracksIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTracksCountEndpoint import CompanyCompaniesIdTracksCountEndpoint
from pyconnectwise.models.manage.ContactTrackModel import ContactTrackModel

class CompanyCompaniesIdTracksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tracks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdTracksCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesIdTracksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdTracksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdTracksIdEndpoint: The initialized CompanyCompaniesIdTracksIdEndpoint object.
        """
        child = CompanyCompaniesIdTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactTrackModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/tracks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactTrackModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactTrackModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactTrackModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactTrackModel]: The parsed response data.
        """
        return self._parse_many(ContactTrackModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactTrackModel:
        """
        Performs a POST request against the /company/companies/{parentId}/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactTrackModel: The parsed response data.
        """
        return self._parse_one(ContactTrackModel, super().make_request("POST", params=params).json())
        