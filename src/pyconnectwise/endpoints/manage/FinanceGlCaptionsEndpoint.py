from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceGlCaptionsIdEndpoint import FinanceGlCaptionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceGlCaptionsCountEndpoint import FinanceGlCaptionsCountEndpoint
from pyconnectwise.models.manage.GLCaptionModel import GLCaptionModel

class FinanceGlCaptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glCaptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlCaptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceGlCaptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceGlCaptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceGlCaptionsIdEndpoint: The initialized FinanceGlCaptionsIdEndpoint object.
        """
        child = FinanceGlCaptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GLCaptionModel]:
        """
        Performs a GET request against the /finance/glCaptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLCaptionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            GLCaptionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[GLCaptionModel]:
        """
        Performs a GET request against the /finance/glCaptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GLCaptionModel]: The parsed response data.
        """
        return self._parse_many(GLCaptionModel, super().make_request("GET", params=params).json())
        