from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdNotificationsCountEndpoint import \
    ProcurementPurchaseorderstatusesIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint import \
    ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import PurchaseOrderStatusNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementPurchaseorderstatusesIdNotificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PurchaseOrderStatusNotification], ConnectWiseManageRequestParams],
    IPostable[PurchaseOrderStatusNotification, ConnectWiseManageRequestParams],
    IPaginateable[PurchaseOrderStatusNotification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notifications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[PurchaseOrderStatusNotification])
        IPostable.__init__(self, PurchaseOrderStatusNotification)
        IPaginateable.__init__(self, PurchaseOrderStatusNotification)

        self.count = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint: The initialized ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint object.
        """
        child = ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[PurchaseOrderStatusNotification]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderStatusNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), PurchaseOrderStatusNotification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[PurchaseOrderStatusNotification]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrderStatusNotification]: The parsed response data.
        """
        return self._parse_many(
            PurchaseOrderStatusNotification, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> PurchaseOrderStatusNotification:
        """
        Performs a POST request against the /procurement/purchaseorderstatuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatusNotification: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrderStatusNotification, super()._make_request("POST", data=data, params=params).json()
        )
