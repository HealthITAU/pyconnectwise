from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsCountEndpoint import (
    ProcurementCatalogIdComponentsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsIdEndpoint import (
    ProcurementCatalogIdComponentsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import CatalogComponent
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementCatalogIdComponentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CatalogComponent], ConnectWiseManageRequestParams],
    IPostable[CatalogComponent, ConnectWiseManageRequestParams],
    IPaginateable[CatalogComponent, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "components", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CatalogComponent])
        IPostable.__init__(self, CatalogComponent)
        IPaginateable.__init__(self, CatalogComponent)

        self.count = self._register_child_endpoint(
            ProcurementCatalogIdComponentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ProcurementCatalogIdComponentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdComponentsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementCatalogIdComponentsIdEndpoint: The initialized ProcurementCatalogIdComponentsIdEndpoint object.
        """
        child = ProcurementCatalogIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CatalogComponent]:
        """
        Performs a GET request against the /procurement/catalog/{id}/components endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogComponent]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CatalogComponent, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CatalogComponent]:
        """
        Performs a GET request against the /procurement/catalog/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogComponent]: The parsed response data.
        """
        return self._parse_many(CatalogComponent, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CatalogComponent:
        """
        Performs a POST request against the /procurement/catalog/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogComponent: The parsed response data.
        """
        return self._parse_one(CatalogComponent, super()._make_request("POST", data=data, params=params).json())
