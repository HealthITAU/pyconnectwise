from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesInfoCountEndpoint import (
    CompanyCommunicationtypesInfoCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import CommunicationTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyCommunicationtypesInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CommunicationTypeInfo], ConnectWiseManageRequestParams],
    IPaginateable[CommunicationTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[CommunicationTypeInfo])
        IPaginateable.__init__(self, CommunicationTypeInfo)

        self.count = self._register_child_endpoint(
            CompanyCommunicationtypesInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CommunicationTypeInfo]:
        """
        Performs a GET request against the /company/communicationTypes/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CommunicationTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CommunicationTypeInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[CommunicationTypeInfo]:
        """
        Performs a GET request against the /company/communicationTypes/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CommunicationTypeInfo]: The parsed response data.
        """
        return self._parse_many(
            CommunicationTypeInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
