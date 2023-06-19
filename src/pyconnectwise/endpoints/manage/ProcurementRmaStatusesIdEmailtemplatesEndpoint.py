from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.RmaStatusEmailTemplateModel import RmaStatusEmailTemplateModel

class ProcurementRmaStatusesIdEmailTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaStatusEmailTemplateModel]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{parentId}/emailTemplates/ endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatusEmailTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RmaStatusEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaStatusEmailTemplateModel]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{parentId}/emailTemplates/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaStatusEmailTemplateModel]: The parsed response data.
        """
        return self._parse_many(RmaStatusEmailTemplateModel, super().make_request("GET", params=params).json())
        