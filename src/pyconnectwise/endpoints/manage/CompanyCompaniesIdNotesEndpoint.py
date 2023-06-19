from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesIdEndpoint import CompanyCompaniesIdNotesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesCountEndpoint import CompanyCompaniesIdNotesCountEndpoint
from pyconnectwise.models.manage.CompanyNoteModel import CompanyNoteModel

class CompanyCompaniesIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdNotesIdEndpoint: The initialized CompanyCompaniesIdNotesIdEndpoint object.
        """
        child = CompanyCompaniesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyNoteModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyNoteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyNoteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyNoteModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyNoteModel]: The parsed response data.
        """
        return self._parse_many(CompanyNoteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyNoteModel:
        """
        Performs a POST request against the /company/companies/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyNoteModel: The parsed response data.
        """
        return self._parse_one(CompanyNoteModel, super().make_request("POST", params=params).json())
        