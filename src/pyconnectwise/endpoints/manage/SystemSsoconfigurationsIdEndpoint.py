from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSsoconfigurationsIdRegistertokenEndpoint import (
    SystemSsoconfigurationsIdRegistertokenEndpoint,
)
from pyconnectwise.endpoints.manage.SystemSsoconfigurationsIdSubmitmembersEndpoint import (
    SystemSsoconfigurationsIdSubmitmembersEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import SsoConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemSsoconfigurationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[SsoConfiguration, ConnectWiseManageRequestParams],
    IPatchable[SsoConfiguration, ConnectWiseManageRequestParams],
    IPuttable[SsoConfiguration, ConnectWiseManageRequestParams],
    IPaginateable[SsoConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SsoConfiguration)
        IPatchable.__init__(self, SsoConfiguration)
        IPuttable.__init__(self, SsoConfiguration)
        IPaginateable.__init__(self, SsoConfiguration)

        self.registertoken = self._register_child_endpoint(
            SystemSsoconfigurationsIdRegistertokenEndpoint(client, parent_endpoint=self)
        )
        self.submitmembers = self._register_child_endpoint(
            SystemSsoconfigurationsIdSubmitmembersEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[SsoConfiguration]:
        """
        Performs a GET request against the /system/ssoConfigurations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SsoConfiguration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), SsoConfiguration, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /system/ssoConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SsoConfiguration:
        """
        Performs a GET request against the /system/ssoConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfiguration: The parsed response data.
        """
        return self._parse_one(SsoConfiguration, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> SsoConfiguration:
        """
        Performs a PATCH request against the /system/ssoConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfiguration: The parsed response data.
        """
        return self._parse_one(SsoConfiguration, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SsoConfiguration:
        """
        Performs a PUT request against the /system/ssoConfigurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfiguration: The parsed response data.
        """
        return self._parse_one(SsoConfiguration, super()._make_request("PUT", data=data, params=params).json())
