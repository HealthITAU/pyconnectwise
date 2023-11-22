from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsCountEndpoint import (
    CompanyManageddevicesintegrationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdEndpoint import (
    CompanyManageddevicesintegrationsIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsInfoEndpoint import (
    CompanyManageddevicesintegrationsInfoEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ManagedDevicesIntegration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyManageddevicesintegrationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ManagedDevicesIntegration], ConnectWiseManageRequestParams],
    IPostable[ManagedDevicesIntegration, ConnectWiseManageRequestParams],
    IPaginateable[ManagedDevicesIntegration, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "managedDevicesIntegrations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ManagedDevicesIntegration])
        IPostable.__init__(self, ManagedDevicesIntegration)
        IPaginateable.__init__(self, ManagedDevicesIntegration)

        self.count = self._register_child_endpoint(
            CompanyManageddevicesintegrationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyManageddevicesintegrationsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> CompanyManageddevicesintegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManageddevicesintegrationsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyManageddevicesintegrationsIdEndpoint: The initialized CompanyManageddevicesintegrationsIdEndpoint object.
        """
        child = CompanyManageddevicesintegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ManagedDevicesIntegration]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagedDevicesIntegration, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ManagedDevicesIntegration]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegration]: The parsed response data.
        """
        return self._parse_many(
            ManagedDevicesIntegration, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagedDevicesIntegration:
        """
        Performs a POST request against the /company/managedDevicesIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegration, super()._make_request("POST", data=data, params=params).json()
        )
