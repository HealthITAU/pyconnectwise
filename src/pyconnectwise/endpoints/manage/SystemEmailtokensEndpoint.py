from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailtokensCountEndpoint import SystemEmailtokensCountEndpoint
from pyconnectwise.endpoints.manage.SystemEmailtokensIdEndpoint import SystemEmailtokensIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import EmailToken
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemEmailtokensEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[EmailToken], ConnectWiseManageRequestParams],
    IPaginateable[EmailToken, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "emailTokens", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[EmailToken])
        IPaginateable.__init__(self, EmailToken)

        self.count = self._register_child_endpoint(SystemEmailtokensCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemEmailtokensIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailtokensIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemEmailtokensIdEndpoint: The initialized SystemEmailtokensIdEndpoint object.
        """
        child = SystemEmailtokensIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[EmailToken]:
        """
        Performs a GET request against the /system/emailTokens endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailToken]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), EmailToken, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[EmailToken]:
        """
        Performs a GET request against the /system/emailTokens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailToken]: The parsed response data.
        """
        return self._parse_many(EmailToken, super()._make_request("GET", data=data, params=params).json())
