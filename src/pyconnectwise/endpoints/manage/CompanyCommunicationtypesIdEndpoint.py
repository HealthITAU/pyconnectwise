from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesIdInfoEndpoint import (
    CompanyCommunicationtypesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesIdUsagesEndpoint import (
    CompanyCommunicationtypesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import CommunicationType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyCommunicationtypesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[CommunicationType, ConnectWiseManageRequestParams],
    IPuttable[CommunicationType, ConnectWiseManageRequestParams],
    IPatchable[CommunicationType, ConnectWiseManageRequestParams],
    IPaginateable[CommunicationType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, CommunicationType)
        IPuttable.__init__(self, CommunicationType)
        IPatchable.__init__(self, CommunicationType)
        IPaginateable.__init__(self, CommunicationType)

        self.usages = self._register_child_endpoint(
            CompanyCommunicationtypesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyCommunicationtypesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CommunicationType]:
        """
        Performs a GET request against the /company/communicationTypes/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CommunicationType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CommunicationType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CommunicationType:
        """
        Performs a GET request against the /company/communicationTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommunicationType: The parsed response data.
        """
        return self._parse_one(
            CommunicationType,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /company/communicationTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CommunicationType:
        """
        Performs a PUT request against the /company/communicationTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommunicationType: The parsed response data.
        """
        return self._parse_one(
            CommunicationType,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CommunicationType:
        """
        Performs a PATCH request against the /company/communicationTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommunicationType: The parsed response data.
        """
        return self._parse_one(
            CommunicationType,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
