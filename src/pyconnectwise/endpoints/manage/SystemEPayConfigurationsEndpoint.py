from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemEPayConfigurationsIdEndpoint import SystemEPayConfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemEPayConfigurationsCountEndpoint import SystemEPayConfigurationsCountEndpoint
from pyconnectwise.models.manage.EPayConfigurationModel import EPayConfigurationModel

class SystemEPayConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ePayConfigurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEPayConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemEPayConfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEPayConfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEPayConfigurationsIdEndpoint: The initialized SystemEPayConfigurationsIdEndpoint object.
        """
        child = SystemEPayConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[EPayConfigurationModel]:
        """
        Performs a GET request against the /system/ePayConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EPayConfigurationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            EPayConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EPayConfigurationModel]:
        """
        Performs a GET request against the /system/ePayConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EPayConfigurationModel]: The parsed response data.
        """
        return self._parse_many(EPayConfigurationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EPayConfigurationModel:
        """
        Performs a POST request against the /system/ePayConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EPayConfigurationModel: The parsed response data.
        """
        return self._parse_one(EPayConfigurationModel, super().make_request("POST", params=params).json())
        