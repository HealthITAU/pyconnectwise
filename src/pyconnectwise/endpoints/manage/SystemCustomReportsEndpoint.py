from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemCustomReportsIdEndpoint import SystemCustomReportsIdEndpoint
from pyconnectwise.endpoints.manage.SystemCustomReportsCountEndpoint import SystemCustomReportsCountEndpoint
from pyconnectwise.models.manage.CustomReportModel import CustomReportModel

class SystemCustomReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "customReports", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCustomReportsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemCustomReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCustomReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemCustomReportsIdEndpoint: The initialized SystemCustomReportsIdEndpoint object.
        """
        child = SystemCustomReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CustomReportModel]:
        """
        Performs a GET request against the /system/customReports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CustomReportModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CustomReportModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CustomReportModel]:
        """
        Performs a GET request against the /system/customReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CustomReportModel]: The parsed response data.
        """
        return self._parse_many(CustomReportModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CustomReportModel:
        """
        Performs a POST request against the /system/customReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CustomReportModel: The parsed response data.
        """
        return self._parse_one(CustomReportModel, super().make_request("POST", params=params).json())
        