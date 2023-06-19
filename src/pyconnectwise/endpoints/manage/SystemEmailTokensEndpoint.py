from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemEmailTokensIdEndpoint import SystemEmailTokensIdEndpoint
from pyconnectwise.endpoints.manage.SystemEmailTokensCountEndpoint import SystemEmailTokensCountEndpoint
from pyconnectwise.models.manage.EmailTokenModel import EmailTokenModel

class SystemEmailTokensEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailTokens", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailTokensCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemEmailTokensIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailTokensIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEmailTokensIdEndpoint: The initialized SystemEmailTokensIdEndpoint object.
        """
        child = SystemEmailTokensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[EmailTokenModel]:
        """
        Performs a GET request against the /system/emailTokens endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailTokenModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            EmailTokenModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EmailTokenModel]:
        """
        Performs a GET request against the /system/emailTokens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailTokenModel]: The parsed response data.
        """
        return self._parse_many(EmailTokenModel, super().make_request("GET", params=params).json())
        