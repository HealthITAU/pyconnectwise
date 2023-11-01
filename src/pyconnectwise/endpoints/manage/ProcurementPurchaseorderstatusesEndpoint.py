from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesCountEndpoint import (
    ProcurementPurchaseorderstatusesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdEndpoint import (
    ProcurementPurchaseorderstatusesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import PurchaseOrderStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementPurchaseorderstatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PurchaseOrderStatus], ConnectWiseManageRequestParams],
    IPostable[PurchaseOrderStatus, ConnectWiseManageRequestParams],
    IPaginateable[PurchaseOrderStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "purchaseorderstatuses", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PurchaseOrderStatus])
        IPostable.__init__(self, PurchaseOrderStatus)
        IPaginateable.__init__(self, PurchaseOrderStatus)

        self.count = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseorderstatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseorderstatusesIdEndpoint: The initialized ProcurementPurchaseorderstatusesIdEndpoint object.
        """
        child = ProcurementPurchaseorderstatusesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PurchaseOrderStatus]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PurchaseOrderStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[PurchaseOrderStatus]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrderStatus]: The parsed response data.
        """
        return self._parse_many(
            PurchaseOrderStatus,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrderStatus:
        """
        Performs a POST request against the /procurement/purchaseorderstatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatus: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrderStatus,
            super()._make_request("POST", data=data, params=params).json(),
        )
