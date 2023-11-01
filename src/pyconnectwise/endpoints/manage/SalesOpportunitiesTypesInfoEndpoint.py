from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesInfoCountEndpoint import (
    SalesOpportunitiesTypesInfoCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import OpportunityTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SalesOpportunitiesTypesInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[OpportunityTypeInfo], ConnectWiseManageRequestParams],
    IPaginateable[OpportunityTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[OpportunityTypeInfo])
        IPaginateable.__init__(self, OpportunityTypeInfo)

        self.count = self._register_child_endpoint(
            SalesOpportunitiesTypesInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[OpportunityTypeInfo]:
        """
        Performs a GET request against the /sales/opportunities/types/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OpportunityTypeInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[OpportunityTypeInfo]:
        """
        Performs a GET request against the /sales/opportunities/types/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityTypeInfo]: The parsed response data.
        """
        return self._parse_many(
            OpportunityTypeInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
