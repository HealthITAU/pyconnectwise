from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemKpisCountEndpoint import (
    SystemKpisCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemKpisIdEndpoint import SystemKpisIdEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import KPI
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemKpisEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[KPI], ConnectWiseManageRequestParams],
    IPaginateable[KPI, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "kpis", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[KPI])
        IPaginateable.__init__(self, KPI)

        self.count = self._register_child_endpoint(
            SystemKpisCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemKpisIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemKpisIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemKpisIdEndpoint: The initialized SystemKpisIdEndpoint object.
        """
        child = SystemKpisIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[KPI]:
        """
        Performs a GET request against the /system/kpis endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KPI]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            KPI,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[KPI]:
        """
        Performs a GET request against the /system/kpis endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KPI]: The parsed response data.
        """
        return self._parse_many(
            KPI, super()._make_request("GET", data=data, params=params).json()
        )
