from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMycompanyServicesIdEndpoint import SystemMycompanyServicesIdEndpoint
from pyconnectwise.models.manage.ServiceModel import ServiceModel

class SystemMycompanyServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "services", parent_endpoint=parent_endpoint)
        
    
    
    def id(self, id: int) -> SystemMycompanyServicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyServicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyServicesIdEndpoint: The initialized SystemMycompanyServicesIdEndpoint object.
        """
        child = SystemMycompanyServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceModel]:
        """
        Performs a GET request against the /system/mycompany/services endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceModel]:
        """
        Performs a GET request against the /system/mycompany/services endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceModel]: The parsed response data.
        """
        return self._parse_many(ServiceModel, super().make_request("GET", params=params).json())
        