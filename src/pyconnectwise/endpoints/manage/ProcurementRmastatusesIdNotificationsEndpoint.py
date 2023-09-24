from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdNotificationsCountEndpoint import \
    ProcurementRmastatusesIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdNotificationsIdEndpoint import \
    ProcurementRmastatusesIdNotificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import RmaStatusNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementRmastatusesIdNotificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[RmaStatusNotification], ConnectWiseManageRequestParams],
    IPostable[RmaStatusNotification, ConnectWiseManageRequestParams],
    IPaginateable[RmaStatusNotification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementRmastatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementRmastatusesIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmastatusesIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmastatusesIdNotificationsIdEndpoint: The initialized ProcurementRmastatusesIdNotificationsIdEndpoint object.
        """
        child = ProcurementRmastatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[RmaStatusNotification]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatusNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), RmaStatusNotification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[RmaStatusNotification]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaStatusNotification]: The parsed response data.
        """
        return self._parse_many(RmaStatusNotification, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> RmaStatusNotification:
        """
        Performs a POST request against the /procurement/rmaStatuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatusNotification: The parsed response data.
        """
        return self._parse_one(RmaStatusNotification, super()._make_request("POST", data=data, params=params).json())
