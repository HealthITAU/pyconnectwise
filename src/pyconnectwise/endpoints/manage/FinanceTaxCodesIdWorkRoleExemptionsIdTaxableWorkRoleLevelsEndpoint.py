from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint import FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsCountEndpoint import FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsCountEndpoint
from pyconnectwise.models.manage.TaxableWorkRoleLevelModel import TaxableWorkRoleLevelModel

class FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableWorkRoleLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint: The initialized FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint object.
        """
        child = FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxableWorkRoleLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableWorkRoleLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxableWorkRoleLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableWorkRoleLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableWorkRoleLevelModel]: The parsed response data.
        """
        return self._parse_many(TaxableWorkRoleLevelModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableWorkRoleLevelModel:
        """
        Performs a POST request against the /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableWorkRoleLevelModel: The parsed response data.
        """
        return self._parse_one(TaxableWorkRoleLevelModel, super().make_request("POST", params=params).json())
        