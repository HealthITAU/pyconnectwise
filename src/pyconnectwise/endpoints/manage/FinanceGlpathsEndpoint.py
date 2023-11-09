from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceGlpathsCountEndpoint import FinanceGlpathsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceGlpathsIdEndpoint import FinanceGlpathsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import GLPath
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceGlpathsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[GLPath], ConnectWiseManageRequestParams],
    IPostable[GLPath, ConnectWiseManageRequestParams],
    IPaginateable[GLPath, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "glpaths", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[GLPath])
        IPostable.__init__(self, GLPath)
        IPaginateable.__init__(self, GLPath)

        self.count = self._register_child_endpoint(FinanceGlpathsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> FinanceGlpathsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceGlpathsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceGlpathsIdEndpoint: The initialized FinanceGlpathsIdEndpoint object.
        """
        child = FinanceGlpathsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[GLPath]:
        """
        Performs a GET request against the /finance/glpaths endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLPath]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), GLPath, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[GLPath]:
        """
        Performs a GET request against the /finance/glpaths endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GLPath]: The parsed response data.
        """
        return self._parse_many(GLPath, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> GLPath:
        """
        Performs a POST request against the /finance/glpaths endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLPath: The parsed response data.
        """
        return self._parse_one(GLPath, super()._make_request("POST", data=data, params=params).json())
