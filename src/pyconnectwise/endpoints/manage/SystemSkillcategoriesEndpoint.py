from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSkillcategoriesCountEndpoint import SystemSkillcategoriesCountEndpoint
from pyconnectwise.endpoints.manage.SystemSkillcategoriesIdEndpoint import SystemSkillcategoriesIdEndpoint
from pyconnectwise.models.manage import SkillCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSkillcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "skillCategories", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemSkillcategoriesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemSkillcategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSkillcategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSkillcategoriesIdEndpoint: The initialized SystemSkillcategoriesIdEndpoint object.
        """
        child = SystemSkillcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SkillCategory]:
        """
        Performs a GET request against the /system/skillCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SkillCategory]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SkillCategory, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SkillCategory]:
        """
        Performs a GET request against the /system/skillCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SkillCategory]: The parsed response data.
        """
        return self._parse_many(SkillCategory, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SkillCategory:
        """
        Performs a POST request against the /system/skillCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SkillCategory: The parsed response data.
        """
        return self._parse_one(SkillCategory, super()._make_request("POST", data=data, params=params).json())
