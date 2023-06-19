from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint import CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint
from pyconnectwise.models.manage.PortalConfigurationOpportunitySetupModel import PortalConfigurationOpportunitySetupModel

class CompanyPortalConfigurationsIdOpportunitySetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunitySetups", parent_endpoint=parent_endpoint)
        
    
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint: The initialized CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint object.
        """
        child = CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationOpportunitySetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/opportunitySetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationOpportunitySetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalConfigurationOpportunitySetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfigurationOpportunitySetupModel]:
        """
        Performs a GET request against the /company/portalConfigurations/{parentId}/opportunitySetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationOpportunitySetupModel]: The parsed response data.
        """
        return self._parse_many(PortalConfigurationOpportunitySetupModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationOpportunitySetupModel:
        """
        Performs a PUT request against the /company/portalConfigurations/{parentId}/opportunitySetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationOpportunitySetupModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationOpportunitySetupModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationOpportunitySetupModel:
        """
        Performs a PATCH request against the /company/portalConfigurations/{parentId}/opportunitySetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationOpportunitySetupModel: The parsed response data.
        """
        return self._parse_one(PortalConfigurationOpportunitySetupModel, super().make_request("PATCH", params=params).json())
        