from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactCountEndpoint import (
    CompanyM365contactCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyM365contactIdEndpoint import (
    CompanyM365contactIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import M365Contact
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyM365contactEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[M365Contact], ConnectWiseManageRequestParams],
    IPaginateable[M365Contact, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "m365contact", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[M365Contact])
        IPaginateable.__init__(self, M365Contact)

        self.count = self._register_child_endpoint(
            CompanyM365contactCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyM365contactIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyM365contactIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyM365contactIdEndpoint: The initialized CompanyM365contactIdEndpoint object.
        """
        child = CompanyM365contactIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[M365Contact]:
        """
        Performs a GET request against the /company/m365contact endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[M365Contact]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            M365Contact,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[M365Contact]:
        """
        Performs a GET request against the /company/m365contact endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[M365Contact]: The parsed response data.
        """
        return self._parse_many(
            M365Contact, super()._make_request("GET", data=data, params=params).json()
        )
