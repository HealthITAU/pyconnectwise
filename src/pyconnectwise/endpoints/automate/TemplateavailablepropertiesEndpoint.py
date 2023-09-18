from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechTemplateAvailableProperty
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TemplateavailablepropertiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Templateavailableproperties", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechTemplateAvailableProperty]:
        """
        Performs a GET request against the /Templateavailableproperties endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechTemplateAvailableProperty]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechTemplateAvailableProperty, self, page, page_size, params
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[LabTechTemplateAvailableProperty]:
        """
        Performs a GET request against the /Templateavailableproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechTemplateAvailableProperty]: The parsed response data.
        """
        return self._parse_many(
            LabTechTemplateAvailableProperty, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechTemplateAvailableProperty:
        """
        Performs a POST request against the /Templateavailableproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechTemplateAvailableProperty: The parsed response data.
        """
        return self._parse_one(
            LabTechTemplateAvailableProperty, super()._make_request("POST", data=data, params=params).json()
        )
