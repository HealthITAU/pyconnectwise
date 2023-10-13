from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogCountEndpoint import ProcurementCatalogCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdEndpoint import ProcurementCatalogIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogInfoEndpoint import ProcurementCatalogInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CatalogItem
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementCatalogEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CatalogItem], ConnectWiseManageRequestParams],
    IPostable[CatalogItem, ConnectWiseManageRequestParams],
    IPaginateable[CatalogItem, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "catalog", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CatalogItem])
        IPostable.__init__(self, CatalogItem)
        IPaginateable.__init__(self, CatalogItem)

        self.count = self._register_child_endpoint(ProcurementCatalogCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementCatalogInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementCatalogIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCatalogIdEndpoint: The initialized ProcurementCatalogIdEndpoint object.
        """
        child = ProcurementCatalogIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CatalogItem]:
        """
        Performs a GET request against the /procurement/catalog endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogItem]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CatalogItem, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CatalogItem]:
        """
        Performs a GET request against the /procurement/catalog endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogItem]: The parsed response data.
        """
        return self._parse_many(CatalogItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CatalogItem:
        """
        Performs a POST request against the /procurement/catalog endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItem: The parsed response data.
        """
        return self._parse_one(CatalogItem, super()._make_request("POST", data=data, params=params).json())
