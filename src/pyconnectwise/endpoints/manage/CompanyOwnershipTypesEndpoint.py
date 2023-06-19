from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyOwnershipTypesIdEndpoint import CompanyOwnershipTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyOwnershipTypesCountEndpoint import CompanyOwnershipTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyOwnershipTypesInfoEndpoint import CompanyOwnershipTypesInfoEndpoint
from pyconnectwise.models.manage.OwnershipTypeModel import OwnershipTypeModel

class CompanyOwnershipTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ownershipTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyOwnershipTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyOwnershipTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyOwnershipTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyOwnershipTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyOwnershipTypesIdEndpoint: The initialized CompanyOwnershipTypesIdEndpoint object.
        """
        child = CompanyOwnershipTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OwnershipTypeModel]:
        """
        Performs a GET request against the /company/ownershipTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OwnershipTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OwnershipTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OwnershipTypeModel]:
        """
        Performs a GET request against the /company/ownershipTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OwnershipTypeModel]: The parsed response data.
        """
        return self._parse_many(OwnershipTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OwnershipTypeModel:
        """
        Performs a POST request against the /company/ownershipTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OwnershipTypeModel: The parsed response data.
        """
        return self._parse_one(OwnershipTypeModel, super().make_request("POST", params=params).json())
        