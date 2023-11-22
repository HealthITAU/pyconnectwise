from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import M365ContactSyncProperty
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyM365contactsyncPropertyIncludedEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[M365ContactSyncProperty], ConnectWiseManageRequestParams],
    IPaginateable[M365ContactSyncProperty, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "included", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[M365ContactSyncProperty])
        IPaginateable.__init__(self, M365ContactSyncProperty)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[M365ContactSyncProperty]:
        """
        Performs a GET request against the /company/m365contactsync/property/included endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[M365ContactSyncProperty]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            M365ContactSyncProperty,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[M365ContactSyncProperty]:
        """
        Performs a GET request against the /company/m365contactsync/property/included endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[M365ContactSyncProperty]: The parsed response data.
        """
        return self._parse_many(
            M365ContactSyncProperty,
            super()._make_request("GET", data=data, params=params).json(),
        )
