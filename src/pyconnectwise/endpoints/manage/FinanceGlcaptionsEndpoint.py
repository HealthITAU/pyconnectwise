from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceGlcaptionsCountEndpoint import FinanceGlcaptionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceGlcaptionsIdEndpoint import FinanceGlcaptionsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import GLCaption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceGlcaptionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[GLCaption], ConnectWiseManageRequestParams],
    IPaginateable[GLCaption, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "glCaptions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[GLCaption])
        IPaginateable.__init__(self, GLCaption)

        self.count = self._register_child_endpoint(FinanceGlcaptionsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> FinanceGlcaptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceGlcaptionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceGlcaptionsIdEndpoint: The initialized FinanceGlcaptionsIdEndpoint object.
        """
        child = FinanceGlcaptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[GLCaption]:
        """
        Performs a GET request against the /finance/glCaptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLCaption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), GLCaption, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[GLCaption]:
        """
        Performs a GET request against the /finance/glCaptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GLCaption]: The parsed response data.
        """
        return self._parse_many(GLCaption, super()._make_request("GET", data=data, params=params).json())
