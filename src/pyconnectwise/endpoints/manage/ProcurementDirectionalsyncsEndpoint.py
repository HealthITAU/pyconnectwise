from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementDirectionalsyncsCountEndpoint import (
    ProcurementDirectionalsyncsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementDirectionalsyncsIdEndpoint import (
    ProcurementDirectionalsyncsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import DirectionalSync
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementDirectionalsyncsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[DirectionalSync], ConnectWiseManageRequestParams],
    IPostable[DirectionalSync, ConnectWiseManageRequestParams],
    IPaginateable[DirectionalSync, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "directionalSyncs", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[DirectionalSync])
        IPostable.__init__(self, DirectionalSync)
        IPaginateable.__init__(self, DirectionalSync)

        self.count = self._register_child_endpoint(
            ProcurementDirectionalsyncsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementDirectionalsyncsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementDirectionalsyncsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementDirectionalsyncsIdEndpoint: The initialized ProcurementDirectionalsyncsIdEndpoint object.
        """
        child = ProcurementDirectionalsyncsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[DirectionalSync]:
        """
        Performs a GET request against the /procurement/directionalSyncs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DirectionalSync]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            DirectionalSync,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[DirectionalSync]:
        """
        Performs a GET request against the /procurement/directionalSyncs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DirectionalSync]: The parsed response data.
        """
        return self._parse_many(
            DirectionalSync,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> DirectionalSync:
        """
        Performs a POST request against the /procurement/directionalSyncs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DirectionalSync: The parsed response data.
        """
        return self._parse_one(
            DirectionalSync,
            super()._make_request("POST", data=data, params=params).json(),
        )
