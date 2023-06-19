from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceTemplatesIdEndpoint import ServiceTemplatesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesCountEndpoint import ServiceTemplatesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTemplatesInfoEndpoint import ServiceTemplatesInfoEndpoint
from pyconnectwise.models.manage.ServiceTemplateModel import ServiceTemplateModel

class ServiceTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "templates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTemplatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTemplatesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceTemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTemplatesIdEndpoint: The initialized ServiceTemplatesIdEndpoint object.
        """
        child = ServiceTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceTemplateModel]:
        """
        Performs a GET request against the /service/templates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceTemplateModel]:
        """
        Performs a GET request against the /service/templates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceTemplateModel]: The parsed response data.
        """
        return self._parse_many(ServiceTemplateModel, super().make_request("GET", params=params).json())
        