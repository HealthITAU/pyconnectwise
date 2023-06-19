from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.ManagementReportSetupModel import ManagementReportSetupModel

class CompanyCompaniesIdManagementReportSetupIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementReportSetupModel:
        """
        Performs a PUT request against the /company/companies/{parentId}/managementReportSetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetupModel: The parsed response data.
        """
        return self._parse_one(ManagementReportSetupModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementReportSetupModel:
        """
        Performs a PATCH request against the /company/companies/{parentId}/managementReportSetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetupModel: The parsed response data.
        """
        return self._parse_one(ManagementReportSetupModel, super().make_request("PATCH", params=params).json())
        