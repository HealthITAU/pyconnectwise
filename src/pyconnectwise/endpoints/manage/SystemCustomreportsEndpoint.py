from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsCountEndpoint import SystemCustomreportsCountEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsIdEndpoint import SystemCustomreportsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import CustomReport
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemCustomreportsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CustomReport], ConnectWiseManageRequestParams],
    IPostable[CustomReport, ConnectWiseManageRequestParams],
    IPaginateable[CustomReport, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "customReports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CustomReport])
        IPostable.__init__(self, CustomReport)
        IPaginateable.__init__(self, CustomReport)

        self.count = self._register_child_endpoint(SystemCustomreportsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemCustomreportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCustomreportsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemCustomreportsIdEndpoint: The initialized SystemCustomreportsIdEndpoint object.
        """
        child = SystemCustomreportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CustomReport]:
        """
        Performs a GET request against the /system/customReports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CustomReport]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CustomReport, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CustomReport]:
        """
        Performs a GET request against the /system/customReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CustomReport]: The parsed response data.
        """
        return self._parse_many(CustomReport, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CustomReport:
        """
        Performs a POST request against the /system/customReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CustomReport: The parsed response data.
        """
        return self._parse_one(CustomReport, super()._make_request("POST", data=data, params=params).json())
