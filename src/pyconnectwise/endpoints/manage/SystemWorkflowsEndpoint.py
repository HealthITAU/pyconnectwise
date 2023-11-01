from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsCountEndpoint import (
    SystemWorkflowsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEndpoint import (
    SystemWorkflowsIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsTabletypesEndpoint import (
    SystemWorkflowsTabletypesEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEndpoint import (
    SystemWorkflowsUserdefinedfieldsEndpoint,
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


class SystemWorkflowsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Workflow], ConnectWiseManageRequestParams],
    IPostable[Workflow, ConnectWiseManageRequestParams],
    IPaginateable[Workflow, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "workflows", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Workflow])
        IPostable.__init__(self, Workflow)
        IPaginateable.__init__(self, Workflow)

        self.table_types = self._register_child_endpoint(
            SystemWorkflowsTabletypesEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(
            SystemWorkflowsCountEndpoint(client, parent_endpoint=self)
        )
        self.userdefinedfields = self._register_child_endpoint(
            SystemWorkflowsUserdefinedfieldsEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemWorkflowsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdEndpoint: The initialized SystemWorkflowsIdEndpoint object.
        """
        child = SystemWorkflowsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Workflow]:
        """
        Performs a GET request against the /system/workflows endpoint and returns an initialized PaginatedResponse object.

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
    ) -> list[Workflow]:
        """
        Performs a GET request against the /system/workflows endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Workflow]: The parsed response data.
        """
        return self._parse_many(
            Workflow, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Workflow:
        """
        Performs a POST request against the /system/workflows endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Workflow: The parsed response data.
        """
        return self._parse_one(
            Workflow, super()._make_request("POST", data=data, params=params).json()
        )
