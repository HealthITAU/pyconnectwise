from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemInfoLinksIdEndpoint import SystemInfoLinksIdEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLinksCountEndpoint import SystemInfoLinksCountEndpoint
from pyconnectwise.models.manage.LinkInfoModel import LinkInfoModel

class SystemInfoLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "links", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoLinksCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemInfoLinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoLinksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoLinksIdEndpoint: The initialized SystemInfoLinksIdEndpoint object.
        """
        child = SystemInfoLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LinkInfoModel]:
        """
        Performs a GET request against the /system/info/links endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LinkInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LinkInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LinkInfoModel]:
        """
        Performs a GET request against the /system/info/links endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LinkInfoModel]: The parsed response data.
        """
        return self._parse_many(LinkInfoModel, super().make_request("GET", params=params).json())
        