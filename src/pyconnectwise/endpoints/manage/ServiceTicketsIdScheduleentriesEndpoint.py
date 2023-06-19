from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceTicketsIdScheduleentriesCountEndpoint import ServiceTicketsIdScheduleentriesCountEndpoint
from pyconnectwise.models.manage.ScheduleEntryReferenceModel import ScheduleEntryReferenceModel

class ServiceTicketsIdScheduleentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "scheduleentries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdScheduleentriesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleEntryReferenceModel]:
        """
        Performs a GET request against the /service/tickets/{parentId}/scheduleentries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleEntryReferenceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleEntryReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleEntryReferenceModel]:
        """
        Performs a GET request against the /service/tickets/{parentId}/scheduleentries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleEntryReferenceModel]: The parsed response data.
        """
        return self._parse_many(ScheduleEntryReferenceModel, super().make_request("GET", params=params).json())
        