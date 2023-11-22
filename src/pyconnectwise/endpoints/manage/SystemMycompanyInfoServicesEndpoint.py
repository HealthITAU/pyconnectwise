from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyInfoServicesIdEndpoint import SystemMycompanyInfoServicesIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import ServiceInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemMycompanyInfoServicesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceInfo], ConnectWiseManageRequestParams],
    IPaginateable[ServiceInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "services", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ServiceInfo])
        IPaginateable.__init__(self, ServiceInfo)

    def id(self, _id: int) -> SystemMycompanyInfoServicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyInfoServicesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemMycompanyInfoServicesIdEndpoint: The initialized SystemMycompanyInfoServicesIdEndpoint object.
        """
        child = SystemMycompanyInfoServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ServiceInfo]:
        """
        Performs a GET request against the /system/mycompany/info/services endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceInfo, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ServiceInfo]:
        """
        Performs a GET request against the /system/mycompany/info/services endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceInfo]: The parsed response data.
        """
        return self._parse_many(ServiceInfo, super()._make_request("GET", data=data, params=params).json())
