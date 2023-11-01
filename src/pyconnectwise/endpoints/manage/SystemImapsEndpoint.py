from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemImapsCountEndpoint import (
    SystemImapsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemImapsIdEndpoint import SystemImapsIdEndpoint
from pyconnectwise.endpoints.manage.SystemImapsInfoEndpoint import (
    SystemImapsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import Imap
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemImapsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Imap], ConnectWiseManageRequestParams],
    IPostable[Imap, ConnectWiseManageRequestParams],
    IPaginateable[Imap, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "imaps", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Imap])
        IPostable.__init__(self, Imap)
        IPaginateable.__init__(self, Imap)

        self.count = self._register_child_endpoint(
            SystemImapsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemImapsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemImapsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemImapsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemImapsIdEndpoint: The initialized SystemImapsIdEndpoint object.
        """
        child = SystemImapsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Imap]:
        """
        Performs a GET request against the /system/imaps endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Imap]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Imap,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Imap]:
        """
        Performs a GET request against the /system/imaps endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Imap]: The parsed response data.
        """
        return self._parse_many(
            Imap, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Imap:
        """
        Performs a POST request against the /system/imaps endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Imap: The parsed response data.
        """
        return self._parse_one(
            Imap, super()._make_request("POST", data=data, params=params).json()
        )
