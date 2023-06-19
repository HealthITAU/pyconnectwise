from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint import FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdTaxableLevelsCountEndpoint import FinanceAccountingUnpostedprocurementIdTaxableLevelsCountEndpoint
from pyconnectwise.models.manage.UnpostedProcurementTaxableLevelModel import UnpostedProcurementTaxableLevelModel

class FinanceAccountingUnpostedprocurementIdTaxableLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedprocurementIdTaxableLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint: The initialized FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint object.
        """
        child = FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnpostedProcurementTaxableLevelModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement/{parentId}/taxableLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedProcurementTaxableLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnpostedProcurementTaxableLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UnpostedProcurementTaxableLevelModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement/{parentId}/taxableLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedProcurementTaxableLevelModel]: The parsed response data.
        """
        return self._parse_many(UnpostedProcurementTaxableLevelModel, super().make_request("GET", params=params).json())
        