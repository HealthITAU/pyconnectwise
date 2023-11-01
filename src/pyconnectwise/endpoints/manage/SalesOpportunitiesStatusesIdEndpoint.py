from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesIdInfoEndpoint import (
    SalesOpportunitiesStatusesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesIdUsagesEndpoint import (
    SalesOpportunitiesStatusesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import OpportunityStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SalesOpportunitiesStatusesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[OpportunityStatus, ConnectWiseManageRequestParams],
    IPuttable[OpportunityStatus, ConnectWiseManageRequestParams],
    IPatchable[OpportunityStatus, ConnectWiseManageRequestParams],
    IPaginateable[OpportunityStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, OpportunityStatus)
        IPuttable.__init__(self, OpportunityStatus)
        IPatchable.__init__(self, OpportunityStatus)
        IPaginateable.__init__(self, OpportunityStatus)

        self.usages = self._register_child_endpoint(
            SalesOpportunitiesStatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SalesOpportunitiesStatusesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[OpportunityStatus]:
        """
        Performs a GET request against the /sales/opportunities/statuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OpportunityStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> OpportunityStatus:
        """
        Performs a GET request against the /sales/opportunities/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStatus: The parsed response data.
        """
        return self._parse_one(
            OpportunityStatus,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /sales/opportunities/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> OpportunityStatus:
        """
        Performs a PUT request against the /sales/opportunities/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStatus: The parsed response data.
        """
        return self._parse_one(
            OpportunityStatus,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> OpportunityStatus:
        """
        Performs a PATCH request against the /sales/opportunities/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityStatus: The parsed response data.
        """
        return self._parse_one(
            OpportunityStatus,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
