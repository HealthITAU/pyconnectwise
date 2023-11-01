from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import ManagedDevicesIntegrationNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyManageddevicesintegrationsIdNotificationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ManagedDevicesIntegrationNotification, ConnectWiseManageRequestParams],
    IPuttable[ManagedDevicesIntegrationNotification, ConnectWiseManageRequestParams],
    IPatchable[ManagedDevicesIntegrationNotification, ConnectWiseManageRequestParams],
    IDeleteable[ConnectWiseManageRequestParams],
    IPaginateable[
        ManagedDevicesIntegrationNotification, ConnectWiseManageRequestParams
    ],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ManagedDevicesIntegrationNotification)
        IPuttable.__init__(self, ManagedDevicesIntegrationNotification)
        IPatchable.__init__(self, ManagedDevicesIntegrationNotification)
        IDeleteable.__init__(self, None)
        IPaginateable.__init__(self, ManagedDevicesIntegrationNotification)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ManagedDevicesIntegrationNotification]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/notifications/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDevicesIntegrationNotification,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagedDevicesIntegrationNotification:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/notifications/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationNotification: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationNotification,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagedDevicesIntegrationNotification:
        """
        Performs a PUT request against the /company/managedDevicesIntegrations/{id}/notifications/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationNotification: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationNotification,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagedDevicesIntegrationNotification:
        """
        Performs a PATCH request against the /company/managedDevicesIntegrations/{id}/notifications/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationNotification: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationNotification,
            super()._make_request("PATCH", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagedDevicesIntegrationNotification:
        """
        Performs a DELETE request against the /company/managedDevicesIntegrations/{id}/notifications/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationNotification: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationNotification,
            super()._make_request("DELETE", data=data, params=params).json(),
        )
