from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsCountEndpoint import (
    SystemWorkflowsIdEventsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdEndpoint import (
    SystemWorkflowsIdEventsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import WorkflowEvent
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemWorkflowsIdEventsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowEvent], ConnectWiseManageRequestParams],
    IPostable[WorkflowEvent, ConnectWiseManageRequestParams],
    IPaginateable[WorkflowEvent, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "events", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[WorkflowEvent])
        IPostable.__init__(self, WorkflowEvent)
        IPaginateable.__init__(self, WorkflowEvent)

        self.count = self._register_child_endpoint(
            SystemWorkflowsIdEventsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemWorkflowsIdEventsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdEventsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdEventsIdEndpoint: The initialized SystemWorkflowsIdEventsIdEndpoint object.
        """
        child = SystemWorkflowsIdEventsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WorkflowEvent]:
        """
        Performs a GET request against the /system/workflows/{id}/events endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params),
            WorkflowEvent,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[WorkflowEvent]:
        """
        Performs a GET request against the /system/workflows/{id}/events endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowEvent]: The parsed response data.
        """
        return self._parse_many(
            WorkflowEvent, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkflowEvent:
        """
        Performs a POST request against the /system/workflows/{id}/events endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEvent: The parsed response data.
        """
        return self._parse_one(
            WorkflowEvent,
            super()._make_request("POST", data=data, params=params).json(),
        )
