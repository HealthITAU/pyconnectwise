from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdEmailtemplatesEndpoint import \
    ProcurementRmastatusesIdEmailtemplatesEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdInfoEndpoint import ProcurementRmastatusesIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdNotificationsEndpoint import \
    ProcurementRmastatusesIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdUsagesEndpoint import ProcurementRmastatusesIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import RmaStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementRmastatusesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[RmaStatus, ConnectWiseManageRequestParams],
    IPuttable[RmaStatus, ConnectWiseManageRequestParams],
    IPatchable[RmaStatus, ConnectWiseManageRequestParams],
    IPaginateable[RmaStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, RmaStatus)
        IPuttable.__init__(self, RmaStatus)
        IPatchable.__init__(self, RmaStatus)
        IPaginateable.__init__(self, RmaStatus)

        self.emailtemplates = self._register_child_endpoint(
            ProcurementRmastatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.email_templates = self._register_child_endpoint(
            ProcurementRmastatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(ProcurementRmastatusesIdInfoEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(
            ProcurementRmastatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self._register_child_endpoint(
            ProcurementRmastatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[RmaStatus]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), RmaStatus, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> RmaStatus:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> RmaStatus:
        """
        Performs a PUT request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> RmaStatus:
        """
        Performs a PATCH request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("PATCH", data=data, params=params).json())
