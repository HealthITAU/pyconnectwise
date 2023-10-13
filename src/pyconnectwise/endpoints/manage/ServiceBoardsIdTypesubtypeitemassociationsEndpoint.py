from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTypesubtypeitemassociationsCountEndpoint import \
    ServiceBoardsIdTypesubtypeitemassociationsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint import \
    ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardTypeSubTypeItemAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdTypesubtypeitemassociationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardTypeSubTypeItemAssociation], ConnectWiseManageRequestParams],
    IPaginateable[BoardTypeSubTypeItemAssociation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "typeSubTypeItemAssociations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardTypeSubTypeItemAssociation])
        IPaginateable.__init__(self, BoardTypeSubTypeItemAssociation)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdTypesubtypeitemassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint: The initialized ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint object.
        """
        child = ServiceBoardsIdTypesubtypeitemassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardTypeSubTypeItemAssociation]:
        """
        Performs a GET request against the /service/boards/{id}/typeSubTypeItemAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTypeSubTypeItemAssociation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardTypeSubTypeItemAssociation, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BoardTypeSubTypeItemAssociation]:
        """
        Performs a GET request against the /service/boards/{id}/typeSubTypeItemAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardTypeSubTypeItemAssociation]: The parsed response data.
        """
        return self._parse_many(
            BoardTypeSubTypeItemAssociation, super()._make_request("GET", data=data, params=params).json()
        )
