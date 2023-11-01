from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemConnectwisehostedscreensCountEndpoint import (
    SystemConnectwisehostedscreensCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemConnectwisehostedscreensIdEndpoint import (
    SystemConnectwisehostedscreensIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ConnectWiseHostedScreen
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemConnectwisehostedscreensEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConnectWiseHostedScreen], ConnectWiseManageRequestParams],
    IPaginateable[ConnectWiseHostedScreen, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "connectWiseHostedScreens", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ConnectWiseHostedScreen])
        IPaginateable.__init__(self, ConnectWiseHostedScreen)

        self.count = self._register_child_endpoint(
            SystemConnectwisehostedscreensCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemConnectwisehostedscreensIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemConnectwisehostedscreensIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemConnectwisehostedscreensIdEndpoint: The initialized SystemConnectwisehostedscreensIdEndpoint object.
        """
        child = SystemConnectwisehostedscreensIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ConnectWiseHostedScreen]:
        """
        Performs a GET request against the /system/connectWiseHostedScreens endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConnectWiseHostedScreen]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ConnectWiseHostedScreen,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ConnectWiseHostedScreen]:
        """
        Performs a GET request against the /system/connectWiseHostedScreens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConnectWiseHostedScreen]: The parsed response data.
        """
        return self._parse_many(
            ConnectWiseHostedScreen,
            super()._make_request("GET", data=data, params=params).json(),
        )
