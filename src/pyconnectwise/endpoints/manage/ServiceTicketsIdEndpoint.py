from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdActivitiesEndpoint import ServiceTicketsIdActivitiesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdAllnotesEndpoint import ServiceTicketsIdAllnotesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdAttachchildrenEndpoint import ServiceTicketsIdAttachchildrenEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdConfigurationsEndpoint import ServiceTicketsIdConfigurationsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdConvertEndpoint import ServiceTicketsIdConvertEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdDocumentsEndpoint import ServiceTicketsIdDocumentsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdInfoEndpoint import ServiceTicketsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdMergeEndpoint import ServiceTicketsIdMergeEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdNotesEndpoint import ServiceTicketsIdNotesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdProductsEndpoint import ServiceTicketsIdProductsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdScheduleentriesEndpoint import (
    ServiceTicketsIdScheduleentriesEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksEndpoint import ServiceTicketsIdTasksEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTimeentriesEndpoint import ServiceTicketsIdTimeentriesEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import Ticket
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceTicketsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Ticket, ConnectWiseManageRequestParams],
    IPatchable[Ticket, ConnectWiseManageRequestParams],
    IPuttable[Ticket, ConnectWiseManageRequestParams],
    IPaginateable[Ticket, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Ticket)
        IPatchable.__init__(self, Ticket)
        IPuttable.__init__(self, Ticket)
        IPaginateable.__init__(self, Ticket)

        self.tasks = self._register_child_endpoint(ServiceTicketsIdTasksEndpoint(client, parent_endpoint=self))
        self.configurations = self._register_child_endpoint(
            ServiceTicketsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.timeentries = self._register_child_endpoint(
            ServiceTicketsIdTimeentriesEndpoint(client, parent_endpoint=self)
        )
        self.scheduleentries = self._register_child_endpoint(
            ServiceTicketsIdScheduleentriesEndpoint(client, parent_endpoint=self)
        )
        self.attach_children = self._register_child_endpoint(
            ServiceTicketsIdAttachchildrenEndpoint(client, parent_endpoint=self)
        )
        self.activities = self._register_child_endpoint(
            ServiceTicketsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.merge = self._register_child_endpoint(ServiceTicketsIdMergeEndpoint(client, parent_endpoint=self))
        self.all_notes = self._register_child_endpoint(ServiceTicketsIdAllnotesEndpoint(client, parent_endpoint=self))
        self.notes = self._register_child_endpoint(ServiceTicketsIdNotesEndpoint(client, parent_endpoint=self))
        self.products = self._register_child_endpoint(ServiceTicketsIdProductsEndpoint(client, parent_endpoint=self))
        self.convert = self._register_child_endpoint(ServiceTicketsIdConvertEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceTicketsIdInfoEndpoint(client, parent_endpoint=self))
        self.documents = self._register_child_endpoint(ServiceTicketsIdDocumentsEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Ticket]:
        """
        Performs a GET request against the /service/tickets/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Ticket]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Ticket, self, page, page_size, params)

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Ticket:
        """
        Performs a GET request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Ticket:
        """
        Performs a PATCH request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Ticket:
        """
        Performs a PUT request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("PUT", data=data, params=params).json())
