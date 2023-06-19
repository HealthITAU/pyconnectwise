from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceTicketsIdInfoEndpoint import ServiceTicketsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdActivitiesEndpoint import ServiceTicketsIdActivitiesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdAllNotesEndpoint import ServiceTicketsIdAllNotesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdAttachChildrenEndpoint import ServiceTicketsIdAttachChildrenEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdConfigurationsEndpoint import ServiceTicketsIdConfigurationsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdConvertEndpoint import ServiceTicketsIdConvertEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdDocumentsEndpoint import ServiceTicketsIdDocumentsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdMergeEndpoint import ServiceTicketsIdMergeEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdNotesEndpoint import ServiceTicketsIdNotesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdProductsEndpoint import ServiceTicketsIdProductsEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdScheduleentriesEndpoint import ServiceTicketsIdScheduleentriesEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTasksEndpoint import ServiceTicketsIdTasksEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdTimeentriesEndpoint import ServiceTicketsIdTimeentriesEndpoint
from pyconnectwise.models.manage.TicketModel import TicketModel

class ServiceTicketsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            ServiceTicketsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.activities = self.register_child_endpoint(
            ServiceTicketsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.allNotes = self.register_child_endpoint(
            ServiceTicketsIdAllNotesEndpoint(client, parent_endpoint=self)
        )
        self.attachChildren = self.register_child_endpoint(
            ServiceTicketsIdAttachChildrenEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self.register_child_endpoint(
            ServiceTicketsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.convert = self.register_child_endpoint(
            ServiceTicketsIdConvertEndpoint(client, parent_endpoint=self)
        )
        self.documents = self.register_child_endpoint(
            ServiceTicketsIdDocumentsEndpoint(client, parent_endpoint=self)
        )
        self.merge = self.register_child_endpoint(
            ServiceTicketsIdMergeEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            ServiceTicketsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.products = self.register_child_endpoint(
            ServiceTicketsIdProductsEndpoint(client, parent_endpoint=self)
        )
        self.scheduleentries = self.register_child_endpoint(
            ServiceTicketsIdScheduleentriesEndpoint(client, parent_endpoint=self)
        )
        self.tasks = self.register_child_endpoint(
            ServiceTicketsIdTasksEndpoint(client, parent_endpoint=self)
        )
        self.timeentries = self.register_child_endpoint(
            ServiceTicketsIdTimeentriesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TicketModel]:
        """
        Performs a GET request against the /service/tickets/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TicketModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TicketModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TicketModel:
        """
        Performs a GET request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketModel: The parsed response data.
        """
        return self._parse_one(TicketModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TicketModel:
        """
        Performs a PUT request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketModel: The parsed response data.
        """
        return self._parse_one(TicketModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TicketModel:
        """
        Performs a PATCH request against the /service/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketModel: The parsed response data.
        """
        return self._parse_one(TicketModel, super().make_request("PATCH", params=params).json())
        