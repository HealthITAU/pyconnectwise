from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSeveritiesCountEndpoint import (
    ServiceSeveritiesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceSeveritiesIdEndpoint import (
    ServiceSeveritiesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Severity
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceSeveritiesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Severity], ConnectWiseManageRequestParams],
    IPaginateable[Severity, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "severities", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Severity])
        IPaginateable.__init__(self, Severity)

        self.count = self._register_child_endpoint(
            ServiceSeveritiesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceSeveritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSeveritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSeveritiesIdEndpoint: The initialized ServiceSeveritiesIdEndpoint object.
        """
        child = ServiceSeveritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Severity]:
        """
        Performs a GET request against the /service/severities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Severity]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Severity,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Severity]:
        """
        Performs a GET request against the /service/severities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Severity]: The parsed response data.
        """
        return self._parse_many(
            Severity, super()._make_request("GET", data=data, params=params).json()
        )
