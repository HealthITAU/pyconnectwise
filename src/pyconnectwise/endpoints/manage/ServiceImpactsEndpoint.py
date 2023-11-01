from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceImpactsCountEndpoint import (
    ServiceImpactsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceImpactsIdEndpoint import (
    ServiceImpactsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import Impact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceImpactsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Impact], ConnectWiseManageRequestParams],
    IPaginateable[Impact, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "impacts", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Impact])
        IPaginateable.__init__(self, Impact)

        self.count = self._register_child_endpoint(
            ServiceImpactsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceImpactsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServiceImpactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceImpactsIdEndpoint: The initialized ServiceImpactsIdEndpoint object.
        """
        child = ServiceImpactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Impact]:
        """
        Performs a GET request against the /service/impacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Impact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Impact,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Impact]:
        """
        Performs a GET request against the /service/impacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Impact]: The parsed response data.
        """
        return self._parse_many(
            Impact, super()._make_request("GET", data=data, params=params).json()
        )
