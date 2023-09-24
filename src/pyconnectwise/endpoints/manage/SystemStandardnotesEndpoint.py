from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemStandardnotesCountEndpoint import SystemStandardnotesCountEndpoint
from pyconnectwise.endpoints.manage.SystemStandardnotesIdEndpoint import SystemStandardnotesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import StandardNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemStandardnotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[StandardNote], ConnectWiseManageRequestParams],
    IPostable[StandardNote, ConnectWiseManageRequestParams],
    IPaginateable[StandardNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "standardNotes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemStandardnotesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemStandardnotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemStandardnotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemStandardnotesIdEndpoint: The initialized SystemStandardnotesIdEndpoint object.
        """
        child = SystemStandardnotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[StandardNote]:
        """
        Performs a GET request against the /system/standardNotes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[StandardNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), StandardNote, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[StandardNote]:
        """
        Performs a GET request against the /system/standardNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StandardNote]: The parsed response data.
        """
        return self._parse_many(StandardNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> StandardNote:
        """
        Performs a POST request against the /system/standardNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            StandardNote: The parsed response data.
        """
        return self._parse_one(StandardNote, super()._make_request("POST", data=data, params=params).json())
