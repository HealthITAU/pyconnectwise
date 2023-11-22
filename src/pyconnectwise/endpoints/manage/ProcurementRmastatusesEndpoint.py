from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesCountEndpoint import ProcurementRmastatusesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdEndpoint import ProcurementRmastatusesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesInfoEndpoint import ProcurementRmastatusesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import RmaStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementRmastatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[RmaStatus], ConnectWiseManageRequestParams],
    IPostable[RmaStatus, ConnectWiseManageRequestParams],
    IPaginateable[RmaStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "rmaStatuses", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[RmaStatus])
        IPostable.__init__(self, RmaStatus)
        IPaginateable.__init__(self, RmaStatus)

        self.count = self._register_child_endpoint(ProcurementRmastatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementRmastatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ProcurementRmastatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmastatusesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementRmastatusesIdEndpoint: The initialized ProcurementRmastatusesIdEndpoint object.
        """
        child = ProcurementRmastatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[RmaStatus]:
        """
        Performs a GET request against the /procurement/rmaStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), RmaStatus, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[RmaStatus]:
        """
        Performs a GET request against the /procurement/rmaStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaStatus]: The parsed response data.
        """
        return self._parse_many(RmaStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> RmaStatus:
        """
        Performs a POST request against the /procurement/rmaStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("POST", data=data, params=params).json())
