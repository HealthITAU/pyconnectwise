from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeWorkTypesIdEndpoint import TimeWorkTypesIdEndpoint
from pyconnectwise.endpoints.manage.TimeWorkTypesCountEndpoint import TimeWorkTypesCountEndpoint
from pyconnectwise.endpoints.manage.TimeWorkTypesInfoEndpoint import TimeWorkTypesInfoEndpoint
from pyconnectwise.models.manage.WorkTypeModel import WorkTypeModel

class TimeWorkTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            TimeWorkTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeWorkTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeWorkTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeWorkTypesIdEndpoint: The initialized TimeWorkTypesIdEndpoint object.
        """
        child = TimeWorkTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkTypeModel]:
        """
        Performs a GET request against the /time/workTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkTypeModel]:
        """
        Performs a GET request against the /time/workTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkTypeModel]: The parsed response data.
        """
        return self._parse_many(WorkTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkTypeModel:
        """
        Performs a POST request against the /time/workTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkTypeModel: The parsed response data.
        """
        return self._parse_one(WorkTypeModel, super().make_request("POST", params=params).json())
        