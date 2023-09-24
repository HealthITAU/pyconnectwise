from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemCallbacksCountEndpoint import SystemCallbacksCountEndpoint
from pyconnectwise.endpoints.manage.SystemCallbacksIdEndpoint import SystemCallbacksIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CallbackEntry
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemCallbacksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CallbackEntry], ConnectWiseManageRequestParams],
    IPostable[CallbackEntry, ConnectWiseManageRequestParams],
    IPaginateable[CallbackEntry, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "callbacks", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemCallbacksCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemCallbacksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCallbacksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemCallbacksIdEndpoint: The initialized SystemCallbacksIdEndpoint object.
        """
        child = SystemCallbacksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CallbackEntry]:
        """
        Performs a GET request against the /system/callbacks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CallbackEntry]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CallbackEntry, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CallbackEntry]:
        """
        Performs a GET request against the /system/callbacks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CallbackEntry]: The parsed response data.
        """
        return self._parse_many(CallbackEntry, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CallbackEntry:
        """
        Performs a POST request against the /system/callbacks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CallbackEntry: The parsed response data.
        """
        return self._parse_one(CallbackEntry, super()._make_request("POST", data=data, params=params).json())
