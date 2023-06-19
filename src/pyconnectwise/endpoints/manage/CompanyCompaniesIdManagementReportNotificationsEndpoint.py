from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementReportNotificationsIdEndpoint import CompanyCompaniesIdManagementReportNotificationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementReportNotificationsCountEndpoint import CompanyCompaniesIdManagementReportNotificationsCountEndpoint
from pyconnectwise.models.manage.ManagementReportNotificationModel import ManagementReportNotificationModel

class CompanyCompaniesIdManagementReportNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementReportNotifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdManagementReportNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesIdManagementReportNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdManagementReportNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdManagementReportNotificationsIdEndpoint: The initialized CompanyCompaniesIdManagementReportNotificationsIdEndpoint object.
        """
        child = CompanyCompaniesIdManagementReportNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagementReportNotificationModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/managementReportNotifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementReportNotificationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagementReportNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementReportNotificationModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/managementReportNotifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementReportNotificationModel]: The parsed response data.
        """
        return self._parse_many(ManagementReportNotificationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementReportNotificationModel:
        """
        Performs a POST request against the /company/companies/{parentId}/managementReportNotifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportNotificationModel: The parsed response data.
        """
        return self._parse_one(ManagementReportNotificationModel, super().make_request("POST", params=params).json())
        