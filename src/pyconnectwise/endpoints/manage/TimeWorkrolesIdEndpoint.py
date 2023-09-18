from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdInfoEndpoint import TimeWorkrolesIdInfoEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdLocationsEndpoint import TimeWorkrolesIdLocationsEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdUsagesEndpoint import TimeWorkrolesIdUsagesEndpoint
from pyconnectwise.models.manage import WorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeWorkrolesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(TimeWorkrolesIdInfoEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(TimeWorkrolesIdUsagesEndpoint(client, parent_endpoint=self))
        self.locations = self._register_child_endpoint(TimeWorkrolesIdLocationsEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkRole]:
        """
        Performs a GET request against the /time/workRoles/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRole]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), WorkRole, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRole:
        """
        Performs a GET request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(WorkRole, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRole:
        """
        Performs a PUT request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(WorkRole, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRole:
        """
        Performs a PATCH request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(WorkRole, super()._make_request("PATCH", data=data, params=params).json())
