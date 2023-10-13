from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsCountEndpoint import SystemSkillsCountEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsIdEndpoint import SystemSkillsIdEndpoint
from pyconnectwise.endpoints.manage.SystemSkillsInfoEndpoint import SystemSkillsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Skill
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemSkillsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Skill], ConnectWiseManageRequestParams],
    IPostable[Skill, ConnectWiseManageRequestParams],
    IPaginateable[Skill, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "skills", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Skill])
        IPostable.__init__(self, Skill)
        IPaginateable.__init__(self, Skill)

        self.count = self._register_child_endpoint(SystemSkillsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemSkillsInfoEndpoint(client, parent_endpoint=self))

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

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Skill]:
        """
        Performs a GET request against the /system/skills endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Skill]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Skill, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Skill]:
        """
        Performs a GET request against the /system/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Skill]: The parsed response data.
        """
        return self._parse_many(Skill, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Skill:
        """
        Performs a POST request against the /system/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Skill: The parsed response data.
        """
        return self._parse_one(Skill, super()._make_request("POST", data=data, params=params).json())
