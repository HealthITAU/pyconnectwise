from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesCountEndpoint import ExpenseTypesCountEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesIdEndpoint import ExpenseTypesIdEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesInfoEndpoint import ExpenseTypesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ExpenseType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ExpenseTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ExpenseType], ConnectWiseManageRequestParams],
    IPostable[ExpenseType, ConnectWiseManageRequestParams],
    IPaginateable[ExpenseType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ExpenseType])
        IPostable.__init__(self, ExpenseType)
        IPaginateable.__init__(self, ExpenseType)

        self.count = self._register_child_endpoint(ExpenseTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ExpenseTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ExpenseTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseTypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ExpenseTypesIdEndpoint: The initialized ExpenseTypesIdEndpoint object.
        """
        child = ExpenseTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ExpenseType]:
        """
        Performs a GET request against the /expense/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ExpenseType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ExpenseType]:
        """
        Performs a GET request against the /expense/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseType]: The parsed response data.
        """
        return self._parse_many(ExpenseType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ExpenseType:
        """
        Performs a POST request against the /expense/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseType: The parsed response data.
        """
        return self._parse_one(ExpenseType, super()._make_request("POST", data=data, params=params).json())
