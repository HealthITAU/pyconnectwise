from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsCountEndpoint import TimeAccrualsCountEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsIdEndpoint import TimeAccrualsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import TimeAccrual
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class TimeAccrualsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TimeAccrual], ConnectWiseManageRequestParams],
    IPostable[TimeAccrual, ConnectWiseManageRequestParams],
    IPaginateable[TimeAccrual, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "accruals", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TimeAccrual])
        IPostable.__init__(self, TimeAccrual)
        IPaginateable.__init__(self, TimeAccrual)

        self.count = self._register_child_endpoint(TimeAccrualsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> TimeAccrualsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeAccrualsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            TimeAccrualsIdEndpoint: The initialized TimeAccrualsIdEndpoint object.
        """
        child = TimeAccrualsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TimeAccrual]:
        """
        Performs a GET request against the /time/accruals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeAccrual]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimeAccrual, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[TimeAccrual]:
        """
        Performs a GET request against the /time/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeAccrual]: The parsed response data.
        """
        return self._parse_many(TimeAccrual, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TimeAccrual:
        """
        Performs a POST request against the /time/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeAccrual: The parsed response data.
        """
        return self._parse_one(TimeAccrual, super()._make_request("POST", data=data, params=params).json())
