from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesActivitiesTypesIdEndpoint import SalesActivitiesTypesIdEndpoint
from pyconnectwise.endpoints.manage.SalesActivitiesTypesCountEndpoint import SalesActivitiesTypesCountEndpoint
from pyconnectwise.models.manage.ActivityTypeModel import ActivityTypeModel

class SalesActivitiesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesActivitiesTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesActivitiesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesActivitiesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesActivitiesTypesIdEndpoint: The initialized SalesActivitiesTypesIdEndpoint object.
        """
        child = SalesActivitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ActivityTypeModel]:
        """
        Performs a GET request against the /sales/activities/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ActivityTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ActivityTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ActivityTypeModel]:
        """
        Performs a GET request against the /sales/activities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ActivityTypeModel]: The parsed response data.
        """
        return self._parse_many(ActivityTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ActivityTypeModel:
        """
        Performs a POST request against the /sales/activities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ActivityTypeModel: The parsed response data.
        """
        return self._parse_one(ActivityTypeModel, super().make_request("POST", params=params).json())
        