from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemCwtimezonesCountEndpoint import (
    SystemCwtimezonesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemCwtimezonesIdEndpoint import (
    SystemCwtimezonesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import CwTimeZone
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemCwtimezonesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CwTimeZone], ConnectWiseManageRequestParams],
    IPaginateable[CwTimeZone, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "cwTimeZones", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[CwTimeZone])
        IPaginateable.__init__(self, CwTimeZone)

        self.count = self._register_child_endpoint(
            SystemCwtimezonesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemCwtimezonesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCwtimezonesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemCwtimezonesIdEndpoint: The initialized SystemCwtimezonesIdEndpoint object.
        """
        child = SystemCwtimezonesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CwTimeZone]:
        """
        Performs a GET request against the /system/cwTimeZones endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CwTimeZone]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CwTimeZone,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[CwTimeZone]:
        """
        Performs a GET request against the /system/cwTimeZones endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CwTimeZone]: The parsed response data.
        """
        return self._parse_many(
            CwTimeZone, super()._make_request("GET", data=data, params=params).json()
        )
