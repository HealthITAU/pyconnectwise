from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaactionsCountEndpoint import (
    ProcurementRmaactionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementRmaactionsIdEndpoint import (
    ProcurementRmaactionsIdEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementRmaactionsInfoEndpoint import (
    ProcurementRmaactionsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import RmaAction
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementRmaactionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[RmaAction], ConnectWiseManageRequestParams],
    IPostable[RmaAction, ConnectWiseManageRequestParams],
    IPaginateable[RmaAction, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "rmaActions", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[RmaAction])
        IPostable.__init__(self, RmaAction)
        IPaginateable.__init__(self, RmaAction)

        self.count = self._register_child_endpoint(
            ProcurementRmaactionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProcurementRmaactionsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementRmaactionsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmaactionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmaactionsIdEndpoint: The initialized ProcurementRmaactionsIdEndpoint object.
        """
        child = ProcurementRmaactionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[RmaAction]:
        """
        Performs a GET request against the /procurement/rmaActions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaAction]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            RmaAction,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[RmaAction]:
        """
        Performs a GET request against the /procurement/rmaActions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaAction]: The parsed response data.
        """
        return self._parse_many(
            RmaAction, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> RmaAction:
        """
        Performs a POST request against the /procurement/rmaActions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaAction: The parsed response data.
        """
        return self._parse_one(
            RmaAction, super()._make_request("POST", data=data, params=params).json()
        )
