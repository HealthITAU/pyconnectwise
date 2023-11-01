from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalsecuritylevelsCountEndpoint import (
    CompanyPortalsecuritylevelsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalsecuritylevelsIdEndpoint import (
    CompanyPortalsecuritylevelsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import PortalSecurityLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyPortalsecuritylevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalSecurityLevel], ConnectWiseManageRequestParams],
    IPaginateable[PortalSecurityLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "portalSecurityLevels", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PortalSecurityLevel])
        IPaginateable.__init__(self, PortalSecurityLevel)

        self.count = self._register_child_endpoint(
            CompanyPortalsecuritylevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalsecuritylevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalsecuritylevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalsecuritylevelsIdEndpoint: The initialized CompanyPortalsecuritylevelsIdEndpoint object.
        """
        child = CompanyPortalsecuritylevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PortalSecurityLevel]:
        """
        Performs a GET request against the /company/portalSecurityLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalSecurityLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalSecurityLevel,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[PortalSecurityLevel]:
        """
        Performs a GET request against the /company/portalSecurityLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalSecurityLevel]: The parsed response data.
        """
        return self._parse_many(
            PortalSecurityLevel,
            super()._make_request("GET", data=data, params=params).json(),
        )
