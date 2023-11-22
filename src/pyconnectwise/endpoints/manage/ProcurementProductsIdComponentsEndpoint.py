from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdComponentsCountEndpoint import (
    ProcurementProductsIdComponentsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementProductsIdComponentsIdEndpoint import (
    ProcurementProductsIdComponentsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import ProductComponent
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementProductsIdComponentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProductComponent], ConnectWiseManageRequestParams],
    IPostable[list[ProductComponent], ConnectWiseManageRequestParams],
    IPaginateable[ProductComponent, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "components", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProductComponent])
        IPostable.__init__(self, list[ProductComponent])
        IPaginateable.__init__(self, ProductComponent)

        self.count = self._register_child_endpoint(
            ProcurementProductsIdComponentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ProcurementProductsIdComponentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdComponentsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementProductsIdComponentsIdEndpoint: The initialized ProcurementProductsIdComponentsIdEndpoint object.
        """
        child = ProcurementProductsIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProductComponent]:
        """
        Performs a GET request against the /procurement/products/{id}/components endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductComponent]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProductComponent, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProductComponent]:
        """
        Performs a GET request against the /procurement/products/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductComponent]: The parsed response data.
        """
        return self._parse_many(ProductComponent, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProductComponent]:
        """
        Performs a POST request against the /procurement/products/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductComponent]: The parsed response data.
        """
        return self._parse_many(ProductComponent, super()._make_request("POST", data=data, params=params).json())
