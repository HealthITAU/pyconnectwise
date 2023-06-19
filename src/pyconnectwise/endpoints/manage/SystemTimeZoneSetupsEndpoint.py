from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemTimeZoneSetupsIdEndpoint import SystemTimeZoneSetupsIdEndpoint
from pyconnectwise.endpoints.manage.SystemTimeZoneSetupsCountEndpoint import SystemTimeZoneSetupsCountEndpoint
from pyconnectwise.endpoints.manage.SystemTimeZoneSetupsInfoEndpoint import SystemTimeZoneSetupsInfoEndpoint
from pyconnectwise.models.manage.TimeZoneSetupModel import TimeZoneSetupModel

class SystemTimeZoneSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeZoneSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemTimeZoneSetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemTimeZoneSetupsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemTimeZoneSetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemTimeZoneSetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemTimeZoneSetupsIdEndpoint: The initialized SystemTimeZoneSetupsIdEndpoint object.
        """
        child = SystemTimeZoneSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeZoneSetupModel]:
        """
        Performs a GET request against the /system/timeZoneSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeZoneSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimeZoneSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeZoneSetupModel]:
        """
        Performs a GET request against the /system/timeZoneSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeZoneSetupModel]: The parsed response data.
        """
        return self._parse_many(TimeZoneSetupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeZoneSetupModel:
        """
        Performs a POST request against the /system/timeZoneSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeZoneSetupModel: The parsed response data.
        """
        return self._parse_one(TimeZoneSetupModel, super().make_request("POST", params=params).json())
        