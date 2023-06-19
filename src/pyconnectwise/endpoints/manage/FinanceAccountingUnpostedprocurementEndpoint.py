from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdEndpoint import FinanceAccountingUnpostedprocurementIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementCountEndpoint import FinanceAccountingUnpostedprocurementCountEndpoint
from pyconnectwise.models.manage.UnpostedProcurementModel import UnpostedProcurementModel

class FinanceAccountingUnpostedprocurementEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unpostedprocurement", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedprocurementCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingUnpostedprocurementIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedprocurementIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedprocurementIdEndpoint: The initialized FinanceAccountingUnpostedprocurementIdEndpoint object.
        """
        child = FinanceAccountingUnpostedprocurementIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnpostedProcurementModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedProcurementModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnpostedProcurementModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UnpostedProcurementModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedProcurementModel]: The parsed response data.
        """
        return self._parse_many(UnpostedProcurementModel, super().make_request("GET", params=params).json())
        