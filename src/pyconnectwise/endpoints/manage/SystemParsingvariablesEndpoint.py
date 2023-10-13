from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemParsingvariablesCountEndpoint import SystemParsingvariablesCountEndpoint
from pyconnectwise.endpoints.manage.SystemParsingvariablesIdEndpoint import SystemParsingvariablesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ParsingVariable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemParsingvariablesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ParsingVariable], ConnectWiseManageRequestParams],
    IPaginateable[ParsingVariable, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "parsingVariables", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ParsingVariable])
        IPaginateable.__init__(self, ParsingVariable)

        self.count = self._register_child_endpoint(SystemParsingvariablesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemParsingvariablesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemParsingvariablesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemParsingvariablesIdEndpoint: The initialized SystemParsingvariablesIdEndpoint object.
        """
        child = SystemParsingvariablesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ParsingVariable]:
        """
        Performs a GET request against the /system/parsingVariables endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ParsingVariable]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ParsingVariable, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ParsingVariable]:
        """
        Performs a GET request against the /system/parsingVariables endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ParsingVariable]: The parsed response data.
        """
        return self._parse_many(ParsingVariable, super()._make_request("GET", data=data, params=params).json())
