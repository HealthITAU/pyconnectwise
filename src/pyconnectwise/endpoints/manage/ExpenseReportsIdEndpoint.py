from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ExpenseReportsIdReverseEndpoint import ExpenseReportsIdReverseEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdSubmitEndpoint import ExpenseReportsIdSubmitEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdAuditsEndpoint import ExpenseReportsIdAuditsEndpoint
from pyconnectwise.models.manage.ExpenseReportModel import ExpenseReportModel

class ExpenseReportsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.reverse = self.register_child_endpoint(
            ExpenseReportsIdReverseEndpoint(client, parent_endpoint=self)
        )
        self.submit = self.register_child_endpoint(
            ExpenseReportsIdSubmitEndpoint(client, parent_endpoint=self)
        )
        self.audits = self.register_child_endpoint(
            ExpenseReportsIdAuditsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExpenseReportModel]:
        """
        Performs a GET request against the /expense/reports/{id} endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ExpenseReportModel:
        """
        Performs a GET request against the /expense/reports/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseReportModel: The parsed response data.
        """
        return self._parse_one(ExpenseReportModel, super().make_request("GET", params=params).json())
        