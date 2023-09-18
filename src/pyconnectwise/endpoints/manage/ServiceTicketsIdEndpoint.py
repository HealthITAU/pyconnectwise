from typing import Any

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
from pyconnectwise.endpoints.manage.ServiceTicketsIdScheduleentriesEndpoint import \
    ServiceTicketsIdScheduleentriesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksEndpoint import ServiceTicketsIdTasksEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTimeentriesEndpoint import ServiceTicketsIdTimeentriesEndpoint
from pyconnectwise.models.manage import Ticket
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTicketsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.documents = self._register_child_endpoint(ServiceTicketsIdDocumentsEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceTicketsIdInfoEndpoint(client, parent_endpoint=self))
        self.merge = self._register_child_endpoint(ServiceTicketsIdMergeEndpoint(client, parent_endpoint=self))
        self.tasks = self._register_child_endpoint(ServiceTicketsIdTasksEndpoint(client, parent_endpoint=self))
        self.all_notes = self._register_child_endpoint(ServiceTicketsIdAllnotesEndpoint(client, parent_endpoint=self))
        self.attach_children = self._register_child_endpoint(
            ServiceTicketsIdAttachchildrenEndpoint(client, parent_endpoint=self)
        )
        self.notes = self._register_child_endpoint(ServiceTicketsIdNotesEndpoint(client, parent_endpoint=self))
        self.configurations = self._register_child_endpoint(
            ServiceTicketsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.activities = self._register_child_endpoint(
            ServiceTicketsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.scheduleentries = self._register_child_endpoint(
            ServiceTicketsIdScheduleentriesEndpoint(client, parent_endpoint=self)
        )
        self.convert = self._register_child_endpoint(ServiceTicketsIdConvertEndpoint(client, parent_endpoint=self))
        self.timeentries = self._register_child_endpoint(
            ServiceTicketsIdTimeentriesEndpoint(client, parent_endpoint=self)
        )
        self.products = self._register_child_endpoint(ServiceTicketsIdProductsEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Ticket]:
        """
        Performs a GET request against the /service/tickets/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Ticket]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Ticket, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Ticket:
        """
        Performs a GET request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Ticket:
        """
        Performs a PUT request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Ticket:
        """
        Performs a PATCH request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Ticket: The parsed response data.
        """
        return self._parse_one(Ticket, super()._make_request("PATCH", data=data, params=params).json())
