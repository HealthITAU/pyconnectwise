from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdEndpoint import ServiceTicketsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.change_request import ChangeRequestMsg
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ChangeRequestIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ChangeRequestMsg], ConnectWiseManageRequestParams],
    IPaginateable[ChangeRequestMsg, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ChangeRequestMsg])
        IPostable.__init__(self, ChangeRequestMsg)
        IPaginateable.__init__(self, ChangeRequestMsg)

        # TODO - Figure out if there are other endpoints!
        # TODO - Handle the fact that the TLD is different!

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ChangeRequestMsg]:
        """
        Performs a GET request against the /api/change_requests endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChangeRequestMsg]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), ChangeRequestMsg, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ChangeRequestMsg]:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeRequestMsg]: The parsed response data.
        """
        return self._parse_many(ChangeRequestMsg, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ChangeRequestMsg:
        """
        Performs a POST request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChangeRequestMsg: The parsed response data.
        """
        return self._parse_one(ChangeRequestMsg, super()._make_request("POST", data=data, params=params).json())
