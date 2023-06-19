from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceImpactsIdEndpoint import ServiceImpactsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceImpactsCountEndpoint import ServiceImpactsCountEndpoint
from pyconnectwise.models.manage.ImpactModel import ImpactModel

class ServiceImpactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "impacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceImpactsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceImpactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceImpactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceImpactsIdEndpoint: The initialized ServiceImpactsIdEndpoint object.
        """
        child = ServiceImpactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ImpactModel]:
        """
        Performs a GET request against the /service/impacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ImpactModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ImpactModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ImpactModel]:
        """
        Performs a GET request against the /service/impacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ImpactModel]: The parsed response data.
        """
        return self._parse_many(ImpactModel, super().make_request("GET", params=params).json())
        