from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyContactsTypesIdEndpoint import CompanyContactsTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesCountEndpoint import CompanyContactsTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesInfoEndpoint import CompanyContactsTypesInfoEndpoint
from pyconnectwise.models.manage.ContactTypeModel import ContactTypeModel

class CompanyContactsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyContactsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyContactsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsTypesIdEndpoint: The initialized CompanyContactsTypesIdEndpoint object.
        """
        child = CompanyContactsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactTypeModel]:
        """
        Performs a GET request against the /company/contacts/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactTypeModel]:
        """
        Performs a GET request against the /company/contacts/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactTypeModel]: The parsed response data.
        """
        return self._parse_many(ContactTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactTypeModel:
        """
        Performs a POST request against the /company/contacts/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactTypeModel: The parsed response data.
        """
        return self._parse_one(ContactTypeModel, super().make_request("POST", params=params).json())
        