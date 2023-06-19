from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.CompanyFinanceModel import CompanyFinanceModel

class CompanyCompanyFinanceIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyFinanceModel:
        """
        Performs a PUT request against the /company/companyFinance/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyFinanceModel: The parsed response data.
        """
        return self._parse_one(CompanyFinanceModel, super().make_request("PUT", params=params).json())
        