from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdPrioritiesCountEndpoint import (
    ServiceSlasIdPrioritiesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceSlasIdPrioritiesIdEndpoint import (
    ServiceSlasIdPrioritiesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import SLAPriority
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceSlasIdPrioritiesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SLAPriority], ConnectWiseManageRequestParams],
    IPostable[SLAPriority, ConnectWiseManageRequestParams],
    IPaginateable[SLAPriority, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "priorities", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[SLAPriority])
        IPostable.__init__(self, SLAPriority)
        IPaginateable.__init__(self, SLAPriority)

        self.count = self._register_child_endpoint(
            ServiceSlasIdPrioritiesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceSlasIdPrioritiesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServiceSlasIdPrioritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSlasIdPrioritiesIdEndpoint: The initialized ServiceSlasIdPrioritiesIdEndpoint object.
        """
        child = ServiceSlasIdPrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[SLAPriority]:
        """
        Performs a GET request against the /service/SLAs/{id}/priorities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SLAPriority]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SLAPriority,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[SLAPriority]:
        """
        Performs a GET request against the /service/SLAs/{id}/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SLAPriority]: The parsed response data.
        """
        return self._parse_many(
            SLAPriority, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SLAPriority:
        """
        Performs a POST request against the /service/SLAs/{id}/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SLAPriority: The parsed response data.
        """
        return self._parse_one(
            SLAPriority, super()._make_request("POST", data=data, params=params).json()
        )
