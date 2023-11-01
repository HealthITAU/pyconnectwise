from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoassignresourcesEndpoint import (
    ServiceBoardsIdAutoassignresourcesEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutotemplatesEndpoint import (
    ServiceBoardsIdAutotemplatesEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdExcludedmembersEndpoint import (
    ServiceBoardsIdExcludedmembersEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsEndpoint import (
    ServiceBoardsIdItemsEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdNotificationsEndpoint import (
    ServiceBoardsIdNotificationsEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesEndpoint import (
    ServiceBoardsIdStatusesEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesEndpoint import (
    ServiceBoardsIdSubtypesEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsEndpoint import (
    ServiceBoardsIdTeamsEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdTypesEndpoint import (
    ServiceBoardsIdTypesEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdTypesubtypeitemassociationsEndpoint import (
    ServiceBoardsIdTypesubtypeitemassociationsEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdUsagesEndpoint import (
    ServiceBoardsIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Board
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceBoardsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Board, ConnectWiseManageRequestParams],
    IPuttable[Board, ConnectWiseManageRequestParams],
    IPatchable[Board, ConnectWiseManageRequestParams],
    IPaginateable[Board, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Board)
        IPuttable.__init__(self, Board)
        IPatchable.__init__(self, Board)
        IPaginateable.__init__(self, Board)

        self.auto_assign_resources = self._register_child_endpoint(
            ServiceBoardsIdAutoassignresourcesEndpoint(client, parent_endpoint=self)
        )
        self.teams = self._register_child_endpoint(
            ServiceBoardsIdTeamsEndpoint(client, parent_endpoint=self)
        )
        self.type_sub_type_item_associations = self._register_child_endpoint(
            ServiceBoardsIdTypesubtypeitemassociationsEndpoint(
                client, parent_endpoint=self
            )
        )
        self.statuses = self._register_child_endpoint(
            ServiceBoardsIdStatusesEndpoint(client, parent_endpoint=self)
        )
        self.auto_templates = self._register_child_endpoint(
            ServiceBoardsIdAutotemplatesEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            ServiceBoardsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.items = self._register_child_endpoint(
            ServiceBoardsIdItemsEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self._register_child_endpoint(
            ServiceBoardsIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.types = self._register_child_endpoint(
            ServiceBoardsIdTypesEndpoint(client, parent_endpoint=self)
        )
        self.subtypes = self._register_child_endpoint(
            ServiceBoardsIdSubtypesEndpoint(client, parent_endpoint=self)
        )
        self.excluded_members = self._register_child_endpoint(
            ServiceBoardsIdExcludedmembersEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Board]:
        """
        Performs a GET request against the /service/boards/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Board]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Board,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Board:
        """
        Performs a GET request against the /service/boards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Board: The parsed response data.
        """
        return self._parse_one(
            Board, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /service/boards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Board:
        """
        Performs a PUT request against the /service/boards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Board: The parsed response data.
        """
        return self._parse_one(
            Board, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Board:
        """
        Performs a PATCH request against the /service/boards/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Board: The parsed response data.
        """
        return self._parse_one(
            Board, super()._make_request("PATCH", data=data, params=params).json()
        )
