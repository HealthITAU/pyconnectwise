from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCommunicationTypesIdEndpoint import CompanyCommunicationTypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationTypesCountEndpoint import CompanyCommunicationTypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationTypesInfoEndpoint import CompanyCommunicationTypesInfoEndpoint
from pyconnectwise.models.manage.CommunicationTypeModel import CommunicationTypeModel

class CompanyCommunicationTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "communicationTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCommunicationTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyCommunicationTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCommunicationTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCommunicationTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCommunicationTypesIdEndpoint: The initialized CompanyCommunicationTypesIdEndpoint object.
        """
        child = CompanyCommunicationTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CommunicationTypeModel]:
        """
        Performs a GET request against the /company/communicationTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CommunicationTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CommunicationTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CommunicationTypeModel]:
        """
        Performs a GET request against the /company/communicationTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CommunicationTypeModel]: The parsed response data.
        """
        return self._parse_many(CommunicationTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CommunicationTypeModel:
        """
        Performs a POST request against the /company/communicationTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommunicationTypeModel: The parsed response data.
        """
        return self._parse_one(CommunicationTypeModel, super().make_request("POST", params=params).json())
        