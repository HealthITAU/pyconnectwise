from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSsoconfigurationsCountEndpoint import SystemSsoconfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemSsoconfigurationsIdEndpoint import SystemSsoconfigurationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import SsoConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemSsoconfigurationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SsoConfiguration], ConnectWiseManageRequestParams],
    IPostable[SsoConfiguration, ConnectWiseManageRequestParams],
    IPaginateable[SsoConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "ssoConfigurations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SsoConfiguration])
        IPostable.__init__(self, SsoConfiguration)
        IPaginateable.__init__(self, SsoConfiguration)

        self.count = self._register_child_endpoint(SystemSsoconfigurationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemSsoconfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSsoconfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSsoconfigurationsIdEndpoint: The initialized SystemSsoconfigurationsIdEndpoint object.
        """
        child = SystemSsoconfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[SsoConfiguration]:
        """
        Performs a GET request against the /system/ssoConfigurations endpoint and returns an initialized PaginatedResponse object.

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

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[SsoConfiguration]:
        """
        Performs a GET request against the /system/ssoConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SsoConfiguration]: The parsed response data.
        """
        return self._parse_many(SsoConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SsoConfiguration:
        """
        Performs a POST request against the /system/ssoConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfiguration: The parsed response data.
        """
        return self._parse_one(SsoConfiguration, super()._make_request("POST", data=data, params=params).json())
