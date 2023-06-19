from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMyCompanyCrmIdEndpoint import SystemMyCompanyCrmIdEndpoint
from pyconnectwise.endpoints.manage.SystemMyCompanyCrmCountEndpoint import SystemMyCompanyCrmCountEndpoint
from pyconnectwise.endpoints.manage.SystemMyCompanyCrmInfoEndpoint import SystemMyCompanyCrmInfoEndpoint
from pyconnectwise.models.manage.CrmModel import CrmModel

class SystemMyCompanyCrmEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "crm", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyCrmCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemMyCompanyCrmInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMyCompanyCrmIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyCompanyCrmIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyCompanyCrmIdEndpoint: The initialized SystemMyCompanyCrmIdEndpoint object.
        """
        child = SystemMyCompanyCrmIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CrmModel]:
        """
        Performs a GET request against the /system/myCompany/crm endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CrmModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CrmModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CrmModel]:
        """
        Performs a GET request against the /system/myCompany/crm endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CrmModel]: The parsed response data.
        """
        return self._parse_many(CrmModel, super().make_request("GET", params=params).json())
        