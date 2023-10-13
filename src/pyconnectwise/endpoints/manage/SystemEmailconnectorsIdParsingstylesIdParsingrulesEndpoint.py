from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesIdParsingrulesCountEndpoint import \
    SystemEmailconnectorsIdParsingstylesIdParsingrulesCountEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint import \
    SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import EmailConnectorParsingRule
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemEmailconnectorsIdParsingstylesIdParsingrulesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[EmailConnectorParsingRule], ConnectWiseManageRequestParams],
    IPostable[EmailConnectorParsingRule, ConnectWiseManageRequestParams],
    IPaginateable[EmailConnectorParsingRule, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "parsingRules", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[EmailConnectorParsingRule])
        IPostable.__init__(self, EmailConnectorParsingRule)
        IPaginateable.__init__(self, EmailConnectorParsingRule)

        self.count = self._register_child_endpoint(
            SystemEmailconnectorsIdParsingstylesIdParsingrulesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint: The initialized SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint object.
        """
        child = SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[EmailConnectorParsingRule]:
        """
        Performs a GET request against the /system/emailConnectors/{id}/parsingStyles/{id}/parsingRules endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailConnectorParsingRule]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), EmailConnectorParsingRule, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[EmailConnectorParsingRule]:
        """
        Performs a GET request against the /system/emailConnectors/{id}/parsingStyles/{id}/parsingRules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailConnectorParsingRule]: The parsed response data.
        """
        return self._parse_many(
            EmailConnectorParsingRule, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> EmailConnectorParsingRule:
        """
        Performs a POST request against the /system/emailConnectors/{id}/parsingStyles/{id}/parsingRules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnectorParsingRule: The parsed response data.
        """
        return self._parse_one(
            EmailConnectorParsingRule, super()._make_request("POST", data=data, params=params).json()
        )
