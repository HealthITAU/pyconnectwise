from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemReportsIdColumnsEndpoint import SystemReportsIdColumnsEndpoint
from pyconnectwise.endpoints.manage.SystemReportsIdCountEndpoint import SystemReportsIdCountEndpoint
from pyconnectwise.models.manage.ReportDataResponseModel import ReportDataResponseModel

class SystemReportsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{reportName}", parent_endpoint=parent_endpoint)
        
        self.columns = self.register_child_endpoint(
            SystemReportsIdColumnsEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            SystemReportsIdCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ReportDataResponseModel]:
        """
        Performs a GET request against the /system/reports/{reportName} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportDataResponseModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ReportDataResponseModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ReportDataResponseModel:
        """
        Performs a GET request against the /system/reports/{reportName} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportDataResponseModel: The parsed response data.
        """
        return self._parse_one(ReportDataResponseModel, super().make_request("GET", params=params).json())
        