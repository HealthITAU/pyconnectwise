from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceSourcesIdEndpoint import ServiceSourcesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesCountEndpoint import ServiceSourcesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceSourcesInfoEndpoint import ServiceSourcesInfoEndpoint
from pyconnectwise.models.manage.SourceModel import SourceModel

class ServiceSourcesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sources", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSourcesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceSourcesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceSourcesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSourcesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSourcesIdEndpoint: The initialized ServiceSourcesIdEndpoint object.
        """
        child = ServiceSourcesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SourceModel]:
        """
        Performs a GET request against the /service/sources endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SourceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SourceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SourceModel]:
        """
        Performs a GET request against the /service/sources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SourceModel]: The parsed response data.
        """
        return self._parse_many(SourceModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SourceModel:
        """
        Performs a POST request against the /service/sources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SourceModel: The parsed response data.
        """
        return self._parse_one(SourceModel, super().make_request("POST", params=params).json())
        