from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdNotesCountEndpoint import (
    ServiceTicketsIdNotesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceTicketsIdNotesIdEndpoint import (
    ServiceTicketsIdNotesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ServiceNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceTicketsIdNotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceNote], ConnectWiseManageRequestParams],
    IPostable[ServiceNote, ConnectWiseManageRequestParams],
    IPaginateable[ServiceNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "notes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ServiceNote])
        IPostable.__init__(self, ServiceNote)
        IPaginateable.__init__(self, ServiceNote)

        self.count = self._register_child_endpoint(
            ServiceTicketsIdNotesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceTicketsIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsIdNotesIdEndpoint: The initialized ServiceTicketsIdNotesIdEndpoint object.
        """
        child = ServiceTicketsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ServiceNote]:
        """
        Performs a GET request against the /service/tickets/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ServiceNote,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ServiceNote]:
        """
        Performs a GET request against the /service/tickets/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceNote]: The parsed response data.
        """
        return self._parse_many(
            ServiceNote, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceNote:
        """
        Performs a POST request against the /service/tickets/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceNote: The parsed response data.
        """
        return self._parse_one(
            ServiceNote, super()._make_request("POST", data=data, params=params).json()
        )
