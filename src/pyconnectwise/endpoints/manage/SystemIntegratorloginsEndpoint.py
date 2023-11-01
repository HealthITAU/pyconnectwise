from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorloginsCountEndpoint import (
    SystemIntegratorloginsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemIntegratorloginsIdEndpoint import (
    SystemIntegratorloginsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import IntegratorLogin
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemIntegratorloginsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[IntegratorLogin], ConnectWiseManageRequestParams],
    IPostable[IntegratorLogin, ConnectWiseManageRequestParams],
    IPaginateable[IntegratorLogin, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "integratorlogins", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[IntegratorLogin])
        IPostable.__init__(self, IntegratorLogin)
        IPaginateable.__init__(self, IntegratorLogin)

        self.count = self._register_child_endpoint(
            SystemIntegratorloginsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemIntegratorloginsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemIntegratorloginsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemIntegratorloginsIdEndpoint: The initialized SystemIntegratorloginsIdEndpoint object.
        """
        child = SystemIntegratorloginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[IntegratorLogin]:
        """
        Performs a GET request against the /system/integratorlogins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[IntegratorLogin]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            IntegratorLogin,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[IntegratorLogin]:
        """
        Performs a GET request against the /system/integratorlogins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[IntegratorLogin]: The parsed response data.
        """
        return self._parse_many(
            IntegratorLogin,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> IntegratorLogin:
        """
        Performs a POST request against the /system/integratorlogins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IntegratorLogin: The parsed response data.
        """
        return self._parse_one(
            IntegratorLogin,
            super()._make_request("POST", data=data, params=params).json(),
        )
