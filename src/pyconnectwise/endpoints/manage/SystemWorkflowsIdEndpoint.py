from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdAttachmentsEndpoint import (
    SystemWorkflowsIdAttachmentsEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdCopyEndpoint import (
    SystemWorkflowsIdCopyEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsEndpoint import (
    SystemWorkflowsIdEventsEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdNotifytypesEndpoint import (
    SystemWorkflowsIdNotifytypesEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersEndpoint import (
    SystemWorkflowsIdTriggersEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Workflow
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemWorkflowsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Workflow, ConnectWiseManageRequestParams],
    IPuttable[Workflow, ConnectWiseManageRequestParams],
    IPatchable[Workflow, ConnectWiseManageRequestParams],
    IPaginateable[Workflow, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Workflow)
        IPuttable.__init__(self, Workflow)
        IPatchable.__init__(self, Workflow)
        IPaginateable.__init__(self, Workflow)

        self.copy = self._register_child_endpoint(
            SystemWorkflowsIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.notify_types = self._register_child_endpoint(
            SystemWorkflowsIdNotifytypesEndpoint(client, parent_endpoint=self)
        )
        self.attachments = self._register_child_endpoint(
            SystemWorkflowsIdAttachmentsEndpoint(client, parent_endpoint=self)
        )
        self.events = self._register_child_endpoint(
            SystemWorkflowsIdEventsEndpoint(client, parent_endpoint=self)
        )
        self.triggers = self._register_child_endpoint(
            SystemWorkflowsIdTriggersEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Workflow]:
        """
        Performs a GET request against the /system/workflows/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Workflow]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Workflow,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Workflow:
        """
        Performs a GET request against the /system/workflows/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Workflow: The parsed response data.
        """
        return self._parse_one(
            Workflow, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /system/workflows/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Workflow:
        """
        Performs a PUT request against the /system/workflows/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Workflow: The parsed response data.
        """
        return self._parse_one(
            Workflow, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Workflow:
        """
        Performs a PATCH request against the /system/workflows/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Workflow: The parsed response data.
        """
        return self._parse_one(
            Workflow, super()._make_request("PATCH", data=data, params=params).json()
        )
