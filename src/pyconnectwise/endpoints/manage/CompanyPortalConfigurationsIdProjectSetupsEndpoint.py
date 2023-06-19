from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdProjectSetupsIdEndpoint import CompanyPortalConfigurationsIdProjectSetupsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdProjectSetupsCountEndpoint import CompanyPortalConfigurationsIdProjectSetupsCountEndpoint
from pyconnectwise.models.manage.PortalConfigurationProjectSetupModel import PortalConfigurationProjectSetupModel

class CompanyPortalConfigurationsIdProjectSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsIdProjectSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdProjectSetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalConfigurationsIdProjectSetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalConfigurationsIdProjectSetupsIdEndpoint: The initialized CompanyPortalConfigurationsIdProjectSetupsIdEndpoint object.
        """
        child = CompanyPortalConfigurationsIdProjectSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationProjectSetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/projectSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationProjectSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalConfigurationProjectSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfigurationProjectSetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/projectSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationProjectSetupModel]: The parsed response data.
        """
        return self._parse_many(PortalConfigurationProjectSetupModel, super().make_request("GET", params=params).json())
        