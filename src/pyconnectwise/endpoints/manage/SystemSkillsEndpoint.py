from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemSkillsIdEndpoint import SystemSkillsIdEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsCountEndpoint import SystemSkillsCountEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsInfoEndpoint import SystemSkillsInfoEndpoint
from pyconnectwise.models.manage.SkillModel import SkillModel

class SystemSkillsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "skills", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSkillsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemSkillsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemSkillsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSkillsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSkillsIdEndpoint: The initialized SystemSkillsIdEndpoint object.
        """
        child = SystemSkillsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SkillModel]:
        """
        Performs a GET request against the /system/skills endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SkillModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SkillModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SkillModel]:
        """
        Performs a GET request against the /system/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SkillModel]: The parsed response data.
        """
        return self._parse_many(SkillModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SkillModel:
        """
        Performs a POST request against the /system/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SkillModel: The parsed response data.
        """
        return self._parse_one(SkillModel, super().make_request("POST", params=params).json())
        