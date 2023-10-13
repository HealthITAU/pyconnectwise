from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutotemplatesCountEndpoint import \
    ServiceBoardsIdAutotemplatesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutotemplatesIdEndpoint import ServiceBoardsIdAutotemplatesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardAutoTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdAutotemplatesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardAutoTemplate], ConnectWiseManageRequestParams],
    IPostable[BoardAutoTemplate, ConnectWiseManageRequestParams],
    IPaginateable[BoardAutoTemplate, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "autoTemplates", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardAutoTemplate])
        IPostable.__init__(self, BoardAutoTemplate)
        IPaginateable.__init__(self, BoardAutoTemplate)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdAutotemplatesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceBoardsIdAutotemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdAutotemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdAutotemplatesIdEndpoint: The initialized ServiceBoardsIdAutotemplatesIdEndpoint object.
        """
        child = ServiceBoardsIdAutotemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardAutoTemplate]:
        """
        Performs a GET request against the /service/boards/{id}/autoTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardAutoTemplate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardAutoTemplate, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BoardAutoTemplate]:
        """
        Performs a GET request against the /service/boards/{id}/autoTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardAutoTemplate]: The parsed response data.
        """
        return self._parse_many(BoardAutoTemplate, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardAutoTemplate:
        """
        Performs a POST request against the /service/boards/{id}/autoTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardAutoTemplate: The parsed response data.
        """
        return self._parse_one(BoardAutoTemplate, super()._make_request("POST", data=data, params=params).json())
