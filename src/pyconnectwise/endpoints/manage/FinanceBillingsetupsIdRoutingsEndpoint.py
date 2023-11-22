from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsIdRoutingsCountEndpoint import (
    FinanceBillingsetupsIdRoutingsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceBillingsetupsIdRoutingsIdEndpoint import (
    FinanceBillingsetupsIdRoutingsIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import BillingSetupRouting
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceBillingsetupsIdRoutingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BillingSetupRouting], ConnectWiseManageRequestParams],
    IPostable[BillingSetupRouting, ConnectWiseManageRequestParams],
    IPaginateable[BillingSetupRouting, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "routings", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BillingSetupRouting])
        IPostable.__init__(self, BillingSetupRouting)
        IPaginateable.__init__(self, BillingSetupRouting)

        self.count = self._register_child_endpoint(
            FinanceBillingsetupsIdRoutingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> FinanceBillingsetupsIdRoutingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingsetupsIdRoutingsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceBillingsetupsIdRoutingsIdEndpoint: The initialized FinanceBillingsetupsIdRoutingsIdEndpoint object.
        """
        child = FinanceBillingsetupsIdRoutingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BillingSetupRouting]:
        """
        Performs a GET request against the /finance/billingSetups/{id}/routings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingSetupRouting]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BillingSetupRouting, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BillingSetupRouting]:
        """
        Performs a GET request against the /finance/billingSetups/{id}/routings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingSetupRouting]: The parsed response data.
        """
        return self._parse_many(BillingSetupRouting, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> BillingSetupRouting:
        """
        Performs a POST request against the /finance/billingSetups/{id}/routings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingSetupRouting: The parsed response data.
        """
        return self._parse_one(BillingSetupRouting, super()._make_request("POST", data=data, params=params).json())
