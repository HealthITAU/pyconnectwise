from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemReportsIdEndpoint import SystemReportsIdEndpoint
from pyconnectwise.models.manage.ReportModel import ReportModel

class SystemReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reports", parent_endpoint=parent_endpoint)
        
    
    
    def id(self, id: int) -> SystemReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemReportsIdEndpoint: The initialized SystemReportsIdEndpoint object.
        """
        child = SystemReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ReportModel]:
        """
        Performs a GET request against the /system/reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ReportModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ReportModel]:
        """
        Performs a GET request against the /system/reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportModel]: The parsed response data.
        """
        return self._parse_many(ReportModel, super().make_request("GET", params=params).json())
        