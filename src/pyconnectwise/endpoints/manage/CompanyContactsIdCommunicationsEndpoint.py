from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsIdEndpoint import CompanyContactsIdCommunicationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsCountEndpoint import CompanyContactsIdCommunicationsCountEndpoint
from pyconnectwise.models.manage.ContactCommunicationModel import ContactCommunicationModel

class CompanyContactsIdCommunicationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "communications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsIdCommunicationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyContactsIdCommunicationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdCommunicationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdCommunicationsIdEndpoint: The initialized CompanyContactsIdCommunicationsIdEndpoint object.
        """
        child = CompanyContactsIdCommunicationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactCommunicationModel]:
        """
        Performs a GET request against the /company/contacts/{parentId}/communications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactCommunicationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactCommunicationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactCommunicationModel]:
        """
        Performs a GET request against the /company/contacts/{parentId}/communications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactCommunicationModel]: The parsed response data.
        """
        return self._parse_many(ContactCommunicationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactCommunicationModel:
        """
        Performs a POST request against the /company/contacts/{parentId}/communications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactCommunicationModel: The parsed response data.
        """
        return self._parse_one(ContactCommunicationModel, super().make_request("POST", params=params).json())
        