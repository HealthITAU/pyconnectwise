from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesIdParsingrulesCountEndpoint import \
    SystemEmailconnectorsIdParsingstylesIdParsingrulesCountEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint import \
    SystemEmailconnectorsIdParsingstylesIdParsingrulesIdEndpoint
from pyconnectwise.models.manage import EmailConnectorParsingRule
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemEmailconnectorsIdParsingstylesIdParsingrulesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingRules", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), EmailConnectorParsingRule, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EmailConnectorParsingRule]:
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

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailConnectorParsingRule:
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
