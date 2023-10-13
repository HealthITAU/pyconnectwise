from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesCountEndpoint import \
    SystemEmailconnectorsIdParsingstylesCountEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesIdEndpoint import \
    SystemEmailconnectorsIdParsingstylesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import EmailConnectorParsingStyle
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemEmailconnectorsIdParsingstylesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[EmailConnectorParsingStyle], ConnectWiseManageRequestParams],
    IPostable[EmailConnectorParsingStyle, ConnectWiseManageRequestParams],
    IPaginateable[EmailConnectorParsingStyle, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "parsingStyles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[EmailConnectorParsingStyle])
        IPostable.__init__(self, EmailConnectorParsingStyle)
        IPaginateable.__init__(self, EmailConnectorParsingStyle)

        self.count = self._register_child_endpoint(
            SystemEmailconnectorsIdParsingstylesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemEmailconnectorsIdParsingstylesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailconnectorsIdParsingstylesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEmailconnectorsIdParsingstylesIdEndpoint: The initialized SystemEmailconnectorsIdParsingstylesIdEndpoint object.
        """
        child = SystemEmailconnectorsIdParsingstylesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[EmailConnectorParsingStyle]:
        """
        Performs a GET request against the /system/emailConnectors/{id}/parsingStyles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailConnectorParsingStyle]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), EmailConnectorParsingStyle, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[EmailConnectorParsingStyle]:
        """
        Performs a GET request against the /system/emailConnectors/{id}/parsingStyles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailConnectorParsingStyle]: The parsed response data.
        """
        return self._parse_many(
            EmailConnectorParsingStyle, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> EmailConnectorParsingStyle:
        """
        Performs a POST request against the /system/emailConnectors/{id}/parsingStyles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnectorParsingStyle: The parsed response data.
        """
        return self._parse_one(
            EmailConnectorParsingStyle, super()._make_request("POST", data=data, params=params).json()
        )
