from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceSeveritiesIdEndpoint import ServiceSeveritiesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSeveritiesCountEndpoint import ServiceSeveritiesCountEndpoint
from pyconnectwise.models.manage.SeverityModel import SeverityModel

class ServiceSeveritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "severities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSeveritiesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceSeveritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSeveritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSeveritiesIdEndpoint: The initialized ServiceSeveritiesIdEndpoint object.
        """
        child = ServiceSeveritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SeverityModel]:
        """
        Performs a GET request against the /service/severities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SeverityModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SeverityModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SeverityModel]:
        """
        Performs a GET request against the /service/severities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SeverityModel]: The parsed response data.
        """
        return self._parse_many(SeverityModel, super().make_request("GET", params=params).json())
        