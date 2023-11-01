from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportsIdEndpoint import (
    SystemReportsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import Report
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemReportsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Report], ConnectWiseManageRequestParams],
    IPaginateable[Report, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "reports", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Report])
        IPaginateable.__init__(self, Report)

    def id(self, id: int) -> SystemReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemReportsIdEndpoint: The initialized SystemReportsIdEndpoint object.
        """
        child = SystemReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Report]:
        """
        Performs a GET request against the /system/reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Report]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Report,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Report]:
        """
        Performs a GET request against the /system/reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Report]: The parsed response data.
        """
        return self._parse_many(
            Report, super()._make_request("GET", data=data, params=params).json()
        )
