from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Models import TemplateProperty
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TemplatepropertiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Templateproperties", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TemplateProperty]:
        """
        Performs a GET request against the /Templateproperties endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TemplateProperty]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TemplateProperty,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TemplateProperty]:
        """
        Performs a GET request against the /Templateproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TemplateProperty]: The parsed response data.
        """
        return self._parse_many(TemplateProperty, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TemplateProperty:
        """
        Performs a POST request against the /Templateproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TemplateProperty: The parsed response data.
        """
        return self._parse_one(TemplateProperty, super()._make_request("POST", data=data, params=params).json())
