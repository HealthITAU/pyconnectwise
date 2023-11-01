from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import PurchasingDemand
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementPurchasingdemandsEndpoint(
    ConnectWiseEndpoint, IPostable[PurchasingDemand, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "purchasingDemands", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, PurchasingDemand)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchasingDemand:
        """
        Performs a POST request against the /procurement/purchasingDemands endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchasingDemand: The parsed response data.
        """
        return self._parse_one(
            PurchasingDemand,
            super()._make_request("POST", data=data, params=params).json(),
        )
