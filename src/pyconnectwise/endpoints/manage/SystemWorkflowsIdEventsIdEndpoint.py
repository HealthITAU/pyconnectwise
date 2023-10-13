from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdActionsEndpoint import \
    SystemWorkflowsIdEventsIdActionsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdCopyEndpoint import SystemWorkflowsIdEventsIdCopyEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdTestEndpoint import SystemWorkflowsIdEventsIdTestEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import WorkflowEvent
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemWorkflowsIdEventsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[WorkflowEvent, ConnectWiseManageRequestParams],
    IPuttable[WorkflowEvent, ConnectWiseManageRequestParams],
    IPatchable[WorkflowEvent, ConnectWiseManageRequestParams],
    IPaginateable[WorkflowEvent, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, WorkflowEvent)
        IPuttable.__init__(self, WorkflowEvent)
        IPatchable.__init__(self, WorkflowEvent)
        IPaginateable.__init__(self, WorkflowEvent)

        self.copy = self._register_child_endpoint(SystemWorkflowsIdEventsIdCopyEndpoint(client, parent_endpoint=self))
        self.test = self._register_child_endpoint(SystemWorkflowsIdEventsIdTestEndpoint(client, parent_endpoint=self))
        self.actions = self._register_child_endpoint(
            SystemWorkflowsIdEventsIdActionsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkflowEvent]:
        """
        Performs a GET request against the /system/workflows/{id}/events/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowEvent]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowEvent, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> WorkflowEvent:
        """
        Performs a GET request against the /system/workflows/{id}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEvent: The parsed response data.
        """
        return self._parse_one(WorkflowEvent, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /system/workflows/{id}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> WorkflowEvent:
        """
        Performs a PUT request against the /system/workflows/{id}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEvent: The parsed response data.
        """
        return self._parse_one(WorkflowEvent, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> WorkflowEvent:
        """
        Performs a PATCH request against the /system/workflows/{id}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEvent: The parsed response data.
        """
        return self._parse_one(WorkflowEvent, super()._make_request("PATCH", data=data, params=params).json())
