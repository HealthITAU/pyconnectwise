from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsyncsCountEndpoint import (
    ServiceTicketsyncsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceTicketsyncsIdEndpoint import (
    ServiceTicketsyncsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import TicketSync
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceTicketsyncsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TicketSync], ConnectWiseManageRequestParams],
    IPostable[TicketSync, ConnectWiseManageRequestParams],
    IPaginateable[TicketSync, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "ticketSyncs", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TicketSync])
        IPostable.__init__(self, TicketSync)
        IPaginateable.__init__(self, TicketSync)

        self.count = self._register_child_endpoint(
            ServiceTicketsyncsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceTicketsyncsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsyncsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsyncsIdEndpoint: The initialized ServiceTicketsyncsIdEndpoint object.
        """
        child = ServiceTicketsyncsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TicketSync]:
        """
        Performs a GET request against the /service/ticketSyncs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TicketSync]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TicketSync,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TicketSync]:
        """
        Performs a GET request against the /service/ticketSyncs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TicketSync]: The parsed response data.
        """
        return self._parse_many(
            TicketSync, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TicketSync:
        """
        Performs a POST request against the /service/ticketSyncs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketSync: The parsed response data.
        """
        return self._parse_one(
            TicketSync, super()._make_request("POST", data=data, params=params).json()
        )
