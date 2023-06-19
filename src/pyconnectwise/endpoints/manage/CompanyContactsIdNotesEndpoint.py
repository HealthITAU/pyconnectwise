from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesIdEndpoint import CompanyContactsIdNotesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesCountEndpoint import CompanyContactsIdNotesCountEndpoint
from pyconnectwise.models.manage.ContactNoteModel import ContactNoteModel

class CompanyContactsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyContactsIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdNotesIdEndpoint: The initialized CompanyContactsIdNotesIdEndpoint object.
        """
        child = CompanyContactsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactNoteModel]:
        """
        Performs a GET request against the /company/contacts/{parentId}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactNoteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactNoteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactNoteModel]:
        """
        Performs a GET request against the /company/contacts/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactNoteModel]: The parsed response data.
        """
        return self._parse_many(ContactNoteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactNoteModel:
        """
        Performs a POST request against the /company/contacts/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactNoteModel: The parsed response data.
        """
        return self._parse_one(ContactNoteModel, super().make_request("POST", params=params).json())
        