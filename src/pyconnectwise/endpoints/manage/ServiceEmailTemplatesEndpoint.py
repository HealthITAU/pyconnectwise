from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceEmailTemplatesIdEndpoint import ServiceEmailTemplatesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailTemplatesCountEndpoint import ServiceEmailTemplatesCountEndpoint
from pyconnectwise.models.manage.ServiceEmailTemplateModel import ServiceEmailTemplateModel

class ServiceEmailTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceEmailTemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceEmailTemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceEmailTemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceEmailTemplatesIdEndpoint: The initialized ServiceEmailTemplatesIdEndpoint object.
        """
        child = ServiceEmailTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceEmailTemplateModel]:
        """
        Performs a GET request against the /service/emailTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceEmailTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceEmailTemplateModel]:
        """
        Performs a GET request against the /service/emailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceEmailTemplateModel]: The parsed response data.
        """
        return self._parse_many(ServiceEmailTemplateModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceEmailTemplateModel:
        """
        Performs a POST request against the /service/emailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceEmailTemplateModel: The parsed response data.
        """
        return self._parse_one(ServiceEmailTemplateModel, super().make_request("POST", params=params).json())
        