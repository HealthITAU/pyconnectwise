from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyContactsIdImageEndpoint import CompanyContactsIdImageEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdPortalSecurityEndpoint import CompanyContactsIdPortalSecurityEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdUsagesEndpoint import CompanyContactsIdUsagesEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsEndpoint import CompanyContactsIdCommunicationsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsEndpoint import CompanyContactsIdGroupsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesEndpoint import CompanyContactsIdNotesEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTracksEndpoint import CompanyContactsIdTracksEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeAssociationsEndpoint import CompanyContactsIdTypeAssociationsEndpoint
from pyconnectwise.models.manage.ContactModel import ContactModel

class CompanyContactsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.image = self.register_child_endpoint(
            CompanyContactsIdImageEndpoint(client, parent_endpoint=self)
        )
        self.portalSecurity = self.register_child_endpoint(
            CompanyContactsIdPortalSecurityEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyContactsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.communications = self.register_child_endpoint(
            CompanyContactsIdCommunicationsEndpoint(client, parent_endpoint=self)
        )
        self.groups = self.register_child_endpoint(
            CompanyContactsIdGroupsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            CompanyContactsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self.register_child_endpoint(
            CompanyContactsIdTracksEndpoint(client, parent_endpoint=self)
        )
        self.typeAssociations = self.register_child_endpoint(
            CompanyContactsIdTypeAssociationsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactModel]:
        """
        Performs a GET request against the /company/contacts/{id} endpoint and returns an initialized PaginatedResponse object.

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
            super().make_request(
                "GET",
                params=params
            ),
            ContactModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactModel:
        """
        Performs a GET request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactModel: The parsed response data.
        """
        return self._parse_one(ContactModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactModel:
        """
        Performs a PUT request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactModel: The parsed response data.
        """
        return self._parse_one(ContactModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactModel:
        """
        Performs a PATCH request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactModel: The parsed response data.
        """
        return self._parse_one(ContactModel, super().make_request("PATCH", params=params).json())
        