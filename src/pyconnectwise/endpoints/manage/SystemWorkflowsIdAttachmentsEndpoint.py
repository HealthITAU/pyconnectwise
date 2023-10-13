from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdAttachmentsCountEndpoint import \
    SystemWorkflowsIdAttachmentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdAttachmentsIdEndpoint import SystemWorkflowsIdAttachmentsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import WorkflowAttachment
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemWorkflowsIdAttachmentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowAttachment], ConnectWiseManageRequestParams],
    IPaginateable[WorkflowAttachment, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "attachments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[WorkflowAttachment])
        IPaginateable.__init__(self, WorkflowAttachment)

        self.count = self._register_child_endpoint(
            SystemWorkflowsIdAttachmentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemWorkflowsIdAttachmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdAttachmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdAttachmentsIdEndpoint: The initialized SystemWorkflowsIdAttachmentsIdEndpoint object.
        """
        child = SystemWorkflowsIdAttachmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkflowAttachment]:
        """
        Performs a GET request against the /system/workflows/{id}/attachments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowAttachment]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowAttachment, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[WorkflowAttachment]:
        """
        Performs a GET request against the /system/workflows/{id}/attachments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowAttachment]: The parsed response data.
        """
        return self._parse_many(WorkflowAttachment, super()._make_request("GET", data=data, params=params).json())
