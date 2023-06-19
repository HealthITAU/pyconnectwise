from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemAudittrailCountEndpoint import SystemAudittrailCountEndpoint
from pyconnectwise.models.manage.AuditTrailEntryModel import AuditTrailEntryModel

class SystemAudittrailEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audittrail", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemAudittrailCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AuditTrailEntryModel]:
        """
        Performs a GET request against the /system/audittrail endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AuditTrailEntryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AuditTrailEntryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AuditTrailEntryModel]:
        """
        Performs a GET request against the /system/audittrail endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AuditTrailEntryModel]: The parsed response data.
        """
        return self._parse_many(AuditTrailEntryModel, super().make_request("GET", params=params).json())
        