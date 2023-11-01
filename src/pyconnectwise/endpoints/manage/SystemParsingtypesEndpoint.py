from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemParsingtypesCountEndpoint import (
    SystemParsingtypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemParsingtypesIdEndpoint import (
    SystemParsingtypesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ParsingType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemParsingtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ParsingType], ConnectWiseManageRequestParams],
    IPaginateable[ParsingType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "parsingTypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ParsingType])
        IPaginateable.__init__(self, ParsingType)

        self.count = self._register_child_endpoint(
            SystemParsingtypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemParsingtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemParsingtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemParsingtypesIdEndpoint: The initialized SystemParsingtypesIdEndpoint object.
        """
        child = SystemParsingtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ParsingType]:
        """
        Performs a GET request against the /system/parsingTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ParsingType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ParsingType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ParsingType]:
        """
        Performs a GET request against the /system/parsingTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ParsingType]: The parsed response data.
        """
        return self._parse_many(
            ParsingType, super()._make_request("GET", data=data, params=params).json()
        )
