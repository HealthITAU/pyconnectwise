from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import ManagedDevicesIntegrationCrossReference
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint(
    ConnectWiseEndpoint,
    IDeleteable[ConnectWiseManageRequestParams],
    IGettable[ManagedDevicesIntegrationCrossReference, ConnectWiseManageRequestParams],
    IPatchable[ManagedDevicesIntegrationCrossReference, ConnectWiseManageRequestParams],
    IPuttable[ManagedDevicesIntegrationCrossReference, ConnectWiseManageRequestParams],
    IPaginateable[ManagedDevicesIntegrationCrossReference, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IDeleteable.__init__(self, None)
        IGettable.__init__(self, ManagedDevicesIntegrationCrossReference)
        IPatchable.__init__(self, ManagedDevicesIntegrationCrossReference)
        IPuttable.__init__(self, ManagedDevicesIntegrationCrossReference)
        IPaginateable.__init__(self, ManagedDevicesIntegrationCrossReference)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ManagedDevicesIntegrationCrossReference]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/crossReferences/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationCrossReference]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDevicesIntegrationCrossReference,
            self,
            page,
            page_size,
            params,
        )

    def delete(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegrationCrossReference:
        """
        Performs a DELETE request against the /company/managedDevicesIntegrations/{id}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReference: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationCrossReference, super()._make_request("DELETE", data=data, params=params).json()
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegrationCrossReference:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReference: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationCrossReference, super()._make_request("GET", data=data, params=params).json()
        )

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegrationCrossReference:
        """
        Performs a PATCH request against the /company/managedDevicesIntegrations/{id}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReference: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationCrossReference, super()._make_request("PATCH", data=data, params=params).json()
        )

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegrationCrossReference:
        """
        Performs a PUT request against the /company/managedDevicesIntegrations/{id}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReference: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationCrossReference, super()._make_request("PUT", data=data, params=params).json()
        )
