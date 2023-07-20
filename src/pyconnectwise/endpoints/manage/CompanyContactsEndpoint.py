from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyContactsIdEndpoint import CompanyContactsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsCountEndpoint import CompanyContactsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDefaultEndpoint import CompanyContactsDefaultEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsEndpoint import CompanyContactsDepartmentsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRelationshipsEndpoint import CompanyContactsRelationshipsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRequestPasswordEndpoint import CompanyContactsRequestPasswordEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesEndpoint import CompanyContactsTypesEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsValidatePortalCredentialsEndpoint import CompanyContactsValidatePortalCredentialsEndpoint
from pyconnectwise.models.manage.ContactModel import ContactModel

class CompanyContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
        self.count = self._register_child_endpoint(
            CompanyContactsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self._register_child_endpoint(
            CompanyContactsDefaultEndpoint(client, parent_endpoint=self)
        )
        self.departments = self._register_child_endpoint(
            CompanyContactsDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.relationships = self._register_child_endpoint(
            CompanyContactsRelationshipsEndpoint(client, parent_endpoint=self)
        )
        self.requestPassword = self._register_child_endpoint(
            CompanyContactsRequestPasswordEndpoint(client, parent_endpoint=self)
        )
        self.types = self._register_child_endpoint(
            CompanyContactsTypesEndpoint(client, parent_endpoint=self)
        )
        self.validatePortalCredentials = self._register_child_endpoint(
            CompanyContactsValidatePortalCredentialsEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdEndpoint: The initialized CompanyContactsIdEndpoint object.
        """
        child = CompanyContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactModel]:
        """
        Performs a GET request against the /company/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request(
                "GET",
                params=params
            ),
            ContactModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactModel]:
        """
        Performs a GET request against the /company/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactModel]: The parsed response data.
        """
        return self._parse_many(ContactModel, super()._make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactModel:
        """
        Performs a POST request against the /company/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactModel: The parsed response data.
        """
        return self._parse_one(ContactModel, super()._make_request("POST", data=data, params=params).json())
        