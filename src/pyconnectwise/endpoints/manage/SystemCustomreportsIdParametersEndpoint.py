from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsIdParametersCountEndpoint import \
    SystemCustomreportsIdParametersCountEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsIdParametersIdEndpoint import \
    SystemCustomreportsIdParametersIdEndpoint
from pyconnectwise.models.manage import CustomReportParameter
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemCustomreportsIdParametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parameters", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemCustomreportsIdParametersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemCustomreportsIdParametersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCustomreportsIdParametersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemCustomreportsIdParametersIdEndpoint: The initialized SystemCustomreportsIdParametersIdEndpoint object.
        """
        child = SystemCustomreportsIdParametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CustomReportParameter]:
        """
        Performs a GET request against the /system/customReports/{id}/parameters endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CustomReportParameter]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CustomReportParameter, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CustomReportParameter]:
        """
        Performs a GET request against the /system/customReports/{id}/parameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CustomReportParameter]: The parsed response data.
        """
        return self._parse_many(CustomReportParameter, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CustomReportParameter:
        """
        Performs a POST request against the /system/customReports/{id}/parameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CustomReportParameter: The parsed response data.
        """
        return self._parse_one(CustomReportParameter, super()._make_request("POST", data=data, params=params).json())
