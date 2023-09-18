from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365EmailsetupsCountEndpoint import \
    SystemOffice365EmailsetupsCountEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365EmailsetupsIdEndpoint import SystemOffice365EmailsetupsIdEndpoint
from pyconnectwise.models.manage import Office365EmailSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemOffice365EmailsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailSetups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemOffice365EmailsetupsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemOffice365EmailsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemOffice365EmailsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemOffice365EmailsetupsIdEndpoint: The initialized SystemOffice365EmailsetupsIdEndpoint object.
        """
        child = SystemOffice365EmailsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[Office365EmailSetup]:
        """
        Performs a GET request against the /system/office365/emailSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Office365EmailSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), Office365EmailSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Office365EmailSetup]:
        """
        Performs a GET request against the /system/office365/emailSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Office365EmailSetup]: The parsed response data.
        """
        return self._parse_many(Office365EmailSetup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Office365EmailSetup:
        """
        Performs a POST request against the /system/office365/emailSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Office365EmailSetup: The parsed response data.
        """
        return self._parse_one(Office365EmailSetup, super()._make_request("POST", data=data, params=params).json())
