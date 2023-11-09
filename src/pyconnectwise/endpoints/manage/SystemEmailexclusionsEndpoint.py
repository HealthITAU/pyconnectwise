from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailexclusionsCountEndpoint import SystemEmailexclusionsCountEndpoint
from pyconnectwise.endpoints.manage.SystemEmailexclusionsIdEndpoint import SystemEmailexclusionsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import EmailExclusion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemEmailexclusionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[EmailExclusion], ConnectWiseManageRequestParams],
    IPostable[EmailExclusion, ConnectWiseManageRequestParams],
    IPaginateable[EmailExclusion, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "emailExclusions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[EmailExclusion])
        IPostable.__init__(self, EmailExclusion)
        IPaginateable.__init__(self, EmailExclusion)

        self.count = self._register_child_endpoint(SystemEmailexclusionsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemEmailexclusionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailexclusionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemEmailexclusionsIdEndpoint: The initialized SystemEmailexclusionsIdEndpoint object.
        """
        child = SystemEmailexclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[EmailExclusion]:
        """
        Performs a GET request against the /system/emailExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailExclusion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), EmailExclusion, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[EmailExclusion]:
        """
        Performs a GET request against the /system/emailExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailExclusion]: The parsed response data.
        """
        return self._parse_many(EmailExclusion, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> EmailExclusion:
        """
        Performs a POST request against the /system/emailExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailExclusion: The parsed response data.
        """
        return self._parse_one(EmailExclusion, super()._make_request("POST", data=data, params=params).json())
