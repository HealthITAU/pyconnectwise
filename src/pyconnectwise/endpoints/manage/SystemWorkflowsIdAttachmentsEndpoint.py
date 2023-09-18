from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdAttachmentsCountEndpoint import \
    SystemWorkflowsIdAttachmentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdAttachmentsIdEndpoint import SystemWorkflowsIdAttachmentsIdEndpoint
from pyconnectwise.models.manage import WorkflowAttachment
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsIdAttachmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "attachments", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowAttachment, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowAttachment]:
        """
        Performs a GET request against the /system/workflows/{id}/attachments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowAttachment]: The parsed response data.
        """
        return self._parse_many(WorkflowAttachment, super()._make_request("GET", data=data, params=params).json())
