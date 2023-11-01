from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsInfoCountEndpoint import (
    CompanyMarketdescriptionsInfoCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import MarketDescriptionInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyMarketdescriptionsInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MarketDescriptionInfo], ConnectWiseManageRequestParams],
    IPaginateable[MarketDescriptionInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[MarketDescriptionInfo])
        IPaginateable.__init__(self, MarketDescriptionInfo)

        self.count = self._register_child_endpoint(
            CompanyMarketdescriptionsInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[MarketDescriptionInfo]:
        """
        Performs a GET request against the /company/marketDescriptions/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MarketDescriptionInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MarketDescriptionInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[MarketDescriptionInfo]:
        """
        Performs a GET request against the /company/marketDescriptions/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MarketDescriptionInfo]: The parsed response data.
        """
        return self._parse_many(
            MarketDescriptionInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
