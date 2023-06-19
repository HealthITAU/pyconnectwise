from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemLdapConfigurationsIdEndpoint import SystemLdapConfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemLdapConfigurationsCountEndpoint import SystemLdapConfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemLdapConfigurationsInfoEndpoint import SystemLdapConfigurationsInfoEndpoint
from pyconnectwise.endpoints.manage.SystemLdapConfigurationsTestLinkEndpoint import SystemLdapConfigurationsTestLinkEndpoint
from pyconnectwise.models.manage.LdapConfigurationModel import LdapConfigurationModel

class SystemLdapConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ldapConfigurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLdapConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemLdapConfigurationsInfoEndpoint(client, parent_endpoint=self)
        )
        self.testLink = self.register_child_endpoint(
            SystemLdapConfigurationsTestLinkEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemLdapConfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLdapConfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLdapConfigurationsIdEndpoint: The initialized SystemLdapConfigurationsIdEndpoint object.
        """
        child = SystemLdapConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LdapConfigurationModel]:
        """
        Performs a GET request against the /system/ldapConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LdapConfigurationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LdapConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LdapConfigurationModel]:
        """
        Performs a GET request against the /system/ldapConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LdapConfigurationModel]: The parsed response data.
        """
        return self._parse_many(LdapConfigurationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LdapConfigurationModel:
        """
        Performs a POST request against the /system/ldapConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LdapConfigurationModel: The parsed response data.
        """
        return self._parse_one(LdapConfigurationModel, super().make_request("POST", params=params).json())
        