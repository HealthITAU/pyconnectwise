from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsIdInfoEndpoint import (
    ServiceBoardsIdTeamsIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsIdUsagesEndpoint import (
    ServiceBoardsIdTeamsIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import BoardTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceBoardsIdTeamsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[BoardTeam, ConnectWiseManageRequestParams],
    IPuttable[BoardTeam, ConnectWiseManageRequestParams],
    IPatchable[BoardTeam, ConnectWiseManageRequestParams],
    IPaginateable[BoardTeam, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, BoardTeam)
        IPuttable.__init__(self, BoardTeam)
        IPatchable.__init__(self, BoardTeam)
        IPaginateable.__init__(self, BoardTeam)

        self.usages = self._register_child_endpoint(
            ServiceBoardsIdTeamsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ServiceBoardsIdTeamsIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardTeam]:
        """
        Performs a GET request against the /service/boards/{id}/teams/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTeam]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardTeam,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardTeam:
        """
        Performs a GET request against the /service/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardTeam: The parsed response data.
        """
        return self._parse_one(
            BoardTeam, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /service/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardTeam:
        """
        Performs a PUT request against the /service/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardTeam: The parsed response data.
        """
        return self._parse_one(
            BoardTeam, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardTeam:
        """
        Performs a PATCH request against the /service/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardTeam: The parsed response data.
        """
        return self._parse_one(
            BoardTeam, super()._make_request("PATCH", data=data, params=params).json()
        )
