from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyStatesIdEndpoint import CompanyStatesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyStatesCountEndpoint import CompanyStatesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyStatesInfoEndpoint import CompanyStatesInfoEndpoint
from pyconnectwise.models.manage.StateModel import StateModel

class CompanyStatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "states", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyStatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyStatesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyStatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyStatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyStatesIdEndpoint: The initialized CompanyStatesIdEndpoint object.
        """
        child = CompanyStatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[StateModel]:
        """
        Performs a GET request against the /company/states endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[StateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            StateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[StateModel]:
        """
        Performs a GET request against the /company/states endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StateModel]: The parsed response data.
        """
        return self._parse_many(StateModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> StateModel:
        """
        Performs a POST request against the /company/states endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            StateModel: The parsed response data.
        """
        return self._parse_one(StateModel, super().make_request("POST", params=params).json())
        