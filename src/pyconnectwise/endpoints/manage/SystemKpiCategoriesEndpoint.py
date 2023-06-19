from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemKpiCategoriesIdEndpoint import SystemKpiCategoriesIdEndpoint
from pyconnectwise.endpoints.manage.SystemKpiCategoriesCountEndpoint import SystemKpiCategoriesCountEndpoint
from pyconnectwise.models.manage.KPICategoryModel import KPICategoryModel

class SystemKpiCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "kpiCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemKpiCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemKpiCategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemKpiCategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemKpiCategoriesIdEndpoint: The initialized SystemKpiCategoriesIdEndpoint object.
        """
        child = SystemKpiCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[KPICategoryModel]:
        """
        Performs a GET request against the /system/kpiCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KPICategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            KPICategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KPICategoryModel]:
        """
        Performs a GET request against the /system/kpiCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KPICategoryModel]: The parsed response data.
        """
        return self._parse_many(KPICategoryModel, super().make_request("GET", params=params).json())
        