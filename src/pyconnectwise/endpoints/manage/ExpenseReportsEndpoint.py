from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ExpenseReportsIdEndpoint import ExpenseReportsIdEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsCountEndpoint import ExpenseReportsCountEndpoint
from pyconnectwise.models.manage.ExpenseReportModel import ExpenseReportModel

class ExpenseReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reports", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseReportsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ExpenseReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseReportsIdEndpoint: The initialized ExpenseReportsIdEndpoint object.
        """
        child = ExpenseReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExpenseReportModel]:
        """
        Performs a GET request against the /expense/reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseReportModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ExpenseReportModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseReportModel]:
        """
        Performs a GET request against the /expense/reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseReportModel]: The parsed response data.
        """
        return self._parse_many(ExpenseReportModel, super().make_request("GET", params=params).json())
        