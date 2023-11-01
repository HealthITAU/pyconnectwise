from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceGlaccountsMappedtypesCountEndpoint import (
    FinanceGlaccountsMappedtypesCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import MappedType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceGlaccountsMappedtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MappedType], ConnectWiseManageRequestParams],
    IPaginateable[MappedType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "mappedTypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[MappedType])
        IPaginateable.__init__(self, MappedType)

        self.count = self._register_child_endpoint(
            FinanceGlaccountsMappedtypesCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[MappedType]:
        """
        Performs a GET request against the /finance/glAccounts/mappedTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MappedType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MappedType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[MappedType]:
        """
        Performs a GET request against the /finance/glAccounts/mappedTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MappedType]: The parsed response data.
        """
        return self._parse_many(
            MappedType, super()._make_request("GET", data=data, params=params).json()
        )
