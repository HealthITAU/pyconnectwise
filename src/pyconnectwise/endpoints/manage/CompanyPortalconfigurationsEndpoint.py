from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsCopyEndpoint import (
    CompanyPortalconfigurationsCopyEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsCountEndpoint import (
    CompanyPortalconfigurationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdEndpoint import CompanyPortalconfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupEndpoint import (
    CompanyPortalconfigurationsInvoicesetupEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import PortalConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyPortalconfigurationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalConfiguration], ConnectWiseManageRequestParams],
    IPostable[PortalConfiguration, ConnectWiseManageRequestParams],
    IPaginateable[PortalConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "portalConfigurations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[PortalConfiguration])
        IPostable.__init__(self, PortalConfiguration)
        IPaginateable.__init__(self, PortalConfiguration)

        self.copy = self._register_child_endpoint(CompanyPortalconfigurationsCopyEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsCountEndpoint(client, parent_endpoint=self)
        )
        self.invoice_setup = self._register_child_endpoint(
            CompanyPortalconfigurationsInvoicesetupEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> CompanyPortalconfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdEndpoint: The initialized CompanyPortalconfigurationsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[PortalConfiguration]:
        """
        Performs a GET request against the /company/portalConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfiguration]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalConfiguration, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[PortalConfiguration]:
        """
        Performs a GET request against the /company/portalConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfiguration]: The parsed response data.
        """
        return self._parse_many(PortalConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> PortalConfiguration:
        """
        Performs a POST request against the /company/portalConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfiguration: The parsed response data.
        """
        return self._parse_one(PortalConfiguration, super()._make_request("POST", data=data, params=params).json())
