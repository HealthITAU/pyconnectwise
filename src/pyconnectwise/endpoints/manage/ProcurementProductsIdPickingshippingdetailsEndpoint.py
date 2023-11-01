from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingshippingdetailsCountEndpoint import (
    ProcurementProductsIdPickingshippingdetailsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingshippingdetailsIdEndpoint import (
    ProcurementProductsIdPickingshippingdetailsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ProductPickingShippingDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementProductsIdPickingshippingdetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProductPickingShippingDetail], ConnectWiseManageRequestParams],
    IPostable[list[ProductPickingShippingDetail], ConnectWiseManageRequestParams],
    IPaginateable[ProductPickingShippingDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "pickingShippingDetails", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ProductPickingShippingDetail])
        IPostable.__init__(self, list[ProductPickingShippingDetail])
        IPaginateable.__init__(self, ProductPickingShippingDetail)

        self.count = self._register_child_endpoint(
            ProcurementProductsIdPickingshippingdetailsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> ProcurementProductsIdPickingshippingdetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdPickingshippingdetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementProductsIdPickingshippingdetailsIdEndpoint: The initialized ProcurementProductsIdPickingshippingdetailsIdEndpoint object.
        """
        child = ProcurementProductsIdPickingshippingdetailsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ProductPickingShippingDetail]:
        """
        Performs a GET request against the /procurement/products/{id}/pickingShippingDetails endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductPickingShippingDetail]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProductPickingShippingDetail,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ProductPickingShippingDetail]:
        """
        Performs a GET request against the /procurement/products/{id}/pickingShippingDetails endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductPickingShippingDetail]: The parsed response data.
        """
        return self._parse_many(
            ProductPickingShippingDetail,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ProductPickingShippingDetail]:
        """
        Performs a POST request against the /procurement/products/{id}/pickingShippingDetails endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductPickingShippingDetail]: The parsed response data.
        """
        return self._parse_many(
            ProductPickingShippingDetail,
            super()._make_request("POST", data=data, params=params).json(),
        )
