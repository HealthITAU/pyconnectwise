from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocalesCountEndpoint import SystemInfoLocalesCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocalesIdEndpoint import SystemInfoLocalesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import LocaleInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemInfoLocalesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LocaleInfo], ConnectWiseManageRequestParams],
    IPaginateable[LocaleInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "locales", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LocaleInfo])
        IPaginateable.__init__(self, LocaleInfo)

        self.count = self._register_child_endpoint(SystemInfoLocalesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoLocalesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoLocalesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoLocalesIdEndpoint: The initialized SystemInfoLocalesIdEndpoint object.
        """
        child = SystemInfoLocalesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[LocaleInfo]:
        """
        Performs a GET request against the /system/info/locales endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocaleInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), LocaleInfo, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[LocaleInfo]:
        """
        Performs a GET request against the /system/info/locales endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocaleInfo]: The parsed response data.
        """
        return self._parse_many(LocaleInfo, super()._make_request("GET", data=data, params=params).json())
