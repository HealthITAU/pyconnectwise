from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import ProductDetach
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementProductsIdDetachEndpoint(
    ConnectWiseEndpoint, IPostable[ProductDetach, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "detach", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, ProductDetach)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ProductDetach:
        """
        Performs a POST request against the /procurement/products/{id}/detach endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductDetach: The parsed response data.
        """
        return self._parse_one(
            ProductDetach,
            super()._make_request("POST", data=data, params=params).json(),
        )
