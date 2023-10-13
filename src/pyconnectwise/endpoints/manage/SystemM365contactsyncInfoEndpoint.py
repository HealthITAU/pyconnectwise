from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncInfoCountEndpoint import SystemM365contactsyncInfoCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import M365ContactSyncInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemM365contactsyncInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[M365ContactSyncInfo], ConnectWiseManageRequestParams],
    IPaginateable[M365ContactSyncInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[M365ContactSyncInfo])
        IPaginateable.__init__(self, M365ContactSyncInfo)

        self.count = self._register_child_endpoint(SystemM365contactsyncInfoCountEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[M365ContactSyncInfo]:
        """
        Performs a GET request against the /system/m365contactsync/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[M365ContactSyncInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), M365ContactSyncInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[M365ContactSyncInfo]:
        """
        Performs a GET request against the /system/m365contactsync/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[M365ContactSyncInfo]: The parsed response data.
        """
        return self._parse_many(M365ContactSyncInfo, super()._make_request("GET", data=data, params=params).json())
