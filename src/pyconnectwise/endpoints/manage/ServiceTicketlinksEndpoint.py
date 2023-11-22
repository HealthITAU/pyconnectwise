from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksCountEndpoint import ServiceTicketlinksCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksIdEndpoint import ServiceTicketlinksIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketlinksInfoEndpoint import ServiceTicketlinksInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ServiceTicketLink
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceTicketlinksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceTicketLink], ConnectWiseManageRequestParams],
    IPostable[ServiceTicketLink, ConnectWiseManageRequestParams],
    IPaginateable[ServiceTicketLink, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "ticketLinks", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ServiceTicketLink])
        IPostable.__init__(self, ServiceTicketLink)
        IPaginateable.__init__(self, ServiceTicketLink)

        self.count = self._register_child_endpoint(ServiceTicketlinksCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceTicketlinksInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ServiceTicketlinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketlinksIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ServiceTicketlinksIdEndpoint: The initialized ServiceTicketlinksIdEndpoint object.
        """
        child = ServiceTicketlinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ServiceTicketLink]:
        """
        Performs a GET request against the /service/ticketLinks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTicketLink]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceTicketLink, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ServiceTicketLink]:
        """
        Performs a GET request against the /service/ticketLinks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceTicketLink]: The parsed response data.
        """
        return self._parse_many(ServiceTicketLink, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ServiceTicketLink:
        """
        Performs a POST request against the /service/ticketLinks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceTicketLink: The parsed response data.
        """
        return self._parse_one(ServiceTicketLink, super()._make_request("POST", data=data, params=params).json())
