from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemOffice365EmailSetupsIdEndpoint import SystemOffice365EmailSetupsIdEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365EmailSetupsCountEndpoint import SystemOffice365EmailSetupsCountEndpoint
from pyconnectwise.models.manage.Office365EmailSetupModel import Office365EmailSetupModel

class SystemOffice365EmailSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemOffice365EmailSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemOffice365EmailSetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemOffice365EmailSetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemOffice365EmailSetupsIdEndpoint: The initialized SystemOffice365EmailSetupsIdEndpoint object.
        """
        child = SystemOffice365EmailSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Office365EmailSetupModel]:
        """
        Performs a GET request against the /system/office365/emailSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Office365EmailSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            Office365EmailSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Office365EmailSetupModel]:
        """
        Performs a GET request against the /system/office365/emailSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Office365EmailSetupModel]: The parsed response data.
        """
        return self._parse_many(Office365EmailSetupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Office365EmailSetupModel:
        """
        Performs a POST request against the /system/office365/emailSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Office365EmailSetupModel: The parsed response data.
        """
        return self._parse_one(Office365EmailSetupModel, super().make_request("POST", params=params).json())
        