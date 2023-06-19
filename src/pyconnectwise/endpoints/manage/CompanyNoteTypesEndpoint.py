from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyNoteTypesIdEndpoint import CompanyNoteTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyNoteTypesCountEndpoint import CompanyNoteTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyNoteTypesInfoEndpoint import CompanyNoteTypesInfoEndpoint
from pyconnectwise.models.manage.CompanyNoteTypeModel import CompanyNoteTypeModel

class CompanyNoteTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "noteTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyNoteTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyNoteTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyNoteTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyNoteTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyNoteTypesIdEndpoint: The initialized CompanyNoteTypesIdEndpoint object.
        """
        child = CompanyNoteTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyNoteTypeModel]:
        """
        Performs a GET request against the /company/noteTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyNoteTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyNoteTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyNoteTypeModel]:
        """
        Performs a GET request against the /company/noteTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyNoteTypeModel]: The parsed response data.
        """
        return self._parse_many(CompanyNoteTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyNoteTypeModel:
        """
        Performs a POST request against the /company/noteTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyNoteTypeModel: The parsed response data.
        """
        return self._parse_one(CompanyNoteTypeModel, super().make_request("POST", params=params).json())
        