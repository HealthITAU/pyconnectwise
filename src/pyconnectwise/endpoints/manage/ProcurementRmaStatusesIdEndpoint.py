from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdEmailtemplatesEndpoint import \
    ProcurementRmastatusesIdEmailtemplatesEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdInfoEndpoint import ProcurementRmastatusesIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdNotificationsEndpoint import \
    ProcurementRmastatusesIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdUsagesEndpoint import ProcurementRmastatusesIdUsagesEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import RmaStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementRmastatusesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.notifications = self._register_child_endpoint(
            ProcurementRmastatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.email_templates = self._register_child_endpoint(
            ProcurementRmastatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(ProcurementRmastatusesIdInfoEndpoint(client, parent_endpoint=self))
        self.emailtemplates = self._register_child_endpoint(
            ProcurementRmastatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            ProcurementRmastatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaStatus]:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            RmaStatus,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaStatus:
        """
        Performs a GET request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super()._make_request("DELETE", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaStatus:
        """
        Performs a PUT request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaStatus:
        """
        Performs a PATCH request against the /procurement/rmaStatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaStatus: The parsed response data.
        """
        return self._parse_one(RmaStatus, super()._make_request("PATCH", data=data, params=params).json())
