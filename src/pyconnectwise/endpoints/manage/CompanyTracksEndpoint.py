from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksCountEndpoint import CompanyTracksCountEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdEndpoint import CompanyTracksIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Track
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyTracksEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Track], ConnectWiseManageRequestParams],
    IPostable[Track, ConnectWiseManageRequestParams],
    IPaginateable[Track, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "tracks", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Track])
        IPostable.__init__(self, Track)
        IPaginateable.__init__(self, Track)

        self.count = self._register_child_endpoint(CompanyTracksCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> CompanyTracksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyTracksIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyTracksIdEndpoint: The initialized CompanyTracksIdEndpoint object.
        """
        child = CompanyTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Track]:
        """
        Performs a GET request against the /company/tracks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Track]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Track, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Track]:
        """
        Performs a GET request against the /company/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Track]: The parsed response data.
        """
        return self._parse_many(Track, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Track:
        """
        Performs a POST request against the /company/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Track: The parsed response data.
        """
        return self._parse_one(Track, super()._make_request("POST", data=data, params=params).json())
