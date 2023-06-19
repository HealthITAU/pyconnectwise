from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectTicketsIdTimeentriesCountEndpoint import ProjectTicketsIdTimeentriesCountEndpoint
from pyconnectwise.models.manage.TimeEntryReferenceModel import TimeEntryReferenceModel

class ProjectTicketsIdTimeentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeentries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsIdTimeentriesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeEntryReferenceModel]:
        """
        Performs a GET request against the /project/tickets/{parentId}/timeentries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeEntryReferenceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimeEntryReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeEntryReferenceModel]:
        """
        Performs a GET request against the /project/tickets/{parentId}/timeentries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeEntryReferenceModel]: The parsed response data.
        """
        return self._parse_many(TimeEntryReferenceModel, super().make_request("GET", params=params).json())
        