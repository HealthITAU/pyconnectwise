from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowactionsIdAutomateparametersCountEndpoint import (
    SystemWorkflowactionsIdAutomateparametersCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowactionsIdAutomateparametersIdEndpoint import (
    SystemWorkflowactionsIdAutomateparametersIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import WorkflowActionAutomateParameter
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowactionsIdAutomateparametersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowActionAutomateParameter], ConnectWiseManageRequestParams],
    IPostable[WorkflowActionAutomateParameter, ConnectWiseManageRequestParams],
    IPaginateable[WorkflowActionAutomateParameter, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "automateParameters", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[WorkflowActionAutomateParameter])
        IPostable.__init__(self, WorkflowActionAutomateParameter)
        IPaginateable.__init__(self, WorkflowActionAutomateParameter)

        self.count = self._register_child_endpoint(
            SystemWorkflowactionsIdAutomateparametersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> SystemWorkflowactionsIdAutomateparametersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowactionsIdAutomateparametersIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemWorkflowactionsIdAutomateparametersIdEndpoint: The initialized SystemWorkflowactionsIdAutomateparametersIdEndpoint object.
        """
        child = SystemWorkflowactionsIdAutomateparametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WorkflowActionAutomateParameter]:
        """
        Performs a GET request against the /system/workflowActions/{id}/automateParameters endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowActionAutomateParameter]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), WorkflowActionAutomateParameter, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[WorkflowActionAutomateParameter]:
        """
        Performs a GET request against the /system/workflowActions/{id}/automateParameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowActionAutomateParameter]: The parsed response data.
        """
        return self._parse_many(
            WorkflowActionAutomateParameter, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> WorkflowActionAutomateParameter:
        """
        Performs a POST request against the /system/workflowActions/{id}/automateParameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionAutomateParameter: The parsed response data.
        """
        return self._parse_one(
            WorkflowActionAutomateParameter, super()._make_request("POST", data=data, params=params).json()
        )
