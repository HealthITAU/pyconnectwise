from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint import FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdWorkRoleExemptionsCountEndpoint import FinanceTaxCodesIdWorkRoleExemptionsCountEndpoint
from pyconnectwise.models.manage.WorkRoleExemptionModel import WorkRoleExemptionModel

class FinanceTaxCodesIdWorkRoleExemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExemptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdWorkRoleExemptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint: The initialized FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint object.
        """
        child = FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkRoleExemptionModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/workRoleExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRoleExemptionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkRoleExemptionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkRoleExemptionModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/workRoleExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRoleExemptionModel]: The parsed response data.
        """
        return self._parse_many(WorkRoleExemptionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleExemptionModel:
        """
        Performs a POST request against the /finance/taxCodes/{parentId}/workRoleExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleExemptionModel: The parsed response data.
        """
        return self._parse_one(WorkRoleExemptionModel, super().make_request("POST", params=params).json())
        