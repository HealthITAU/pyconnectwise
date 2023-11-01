from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdAssociationsCountEndpoint import (
    ServiceBoardsIdItemsIdAssociationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdAssociationsIdEndpoint import (
    ServiceBoardsIdItemsIdAssociationsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import BoardItemAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceBoardsIdItemsIdAssociationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardItemAssociation], ConnectWiseManageRequestParams],
    IPaginateable[BoardItemAssociation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "associations", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BoardItemAssociation])
        IPaginateable.__init__(self, BoardItemAssociation)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdItemsIdAssociationsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> ServiceBoardsIdItemsIdAssociationsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdItemsIdAssociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdItemsIdAssociationsIdEndpoint: The initialized ServiceBoardsIdItemsIdAssociationsIdEndpoint object.
        """
        child = ServiceBoardsIdItemsIdAssociationsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardItemAssociation]:
        """
        Performs a GET request against the /service/boards/{id}/items/{id}/associations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardItemAssociation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardItemAssociation,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BoardItemAssociation]:
        """
        Performs a GET request against the /service/boards/{id}/items/{id}/associations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardItemAssociation]: The parsed response data.
        """
        return self._parse_many(
            BoardItemAssociation,
            super()._make_request("GET", data=data, params=params).json(),
        )
