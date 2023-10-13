from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLinksCountEndpoint import SystemInfoLinksCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLinksIdEndpoint import SystemInfoLinksIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import LinkInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemInfoLinksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LinkInfo], ConnectWiseManageRequestParams],
    IPaginateable[LinkInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "links", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LinkInfo])
        IPaginateable.__init__(self, LinkInfo)

        self.count = self._register_child_endpoint(SystemInfoLinksCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoLinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoLinksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoLinksIdEndpoint: The initialized SystemInfoLinksIdEndpoint object.
        """
        child = SystemInfoLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[LinkInfo]:
        """
        Performs a GET request against the /system/info/links endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LinkInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), LinkInfo, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[LinkInfo]:
        """
        Performs a GET request against the /system/info/links endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LinkInfo]: The parsed response data.
        """
        return self._parse_many(LinkInfo, super()._make_request("GET", data=data, params=params).json())
