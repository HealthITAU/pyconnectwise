from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsCountEndpoint import (
    FinanceBillingsetupsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceBillingsetupsIdEndpoint import (
    FinanceBillingsetupsIdEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceBillingsetupsInfoEndpoint import (
    FinanceBillingsetupsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import BillingSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceBillingsetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BillingSetup], ConnectWiseManageRequestParams],
    IPostable[BillingSetup, ConnectWiseManageRequestParams],
    IPaginateable[BillingSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "billingSetups", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BillingSetup])
        IPostable.__init__(self, BillingSetup)
        IPaginateable.__init__(self, BillingSetup)

        self.count = self._register_child_endpoint(
            FinanceBillingsetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            FinanceBillingsetupsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceBillingsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingsetupsIdEndpoint: The initialized FinanceBillingsetupsIdEndpoint object.
        """
        child = FinanceBillingsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BillingSetup]:
        """
        Performs a GET request against the /finance/billingSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BillingSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BillingSetup]:
        """
        Performs a GET request against the /finance/billingSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingSetup]: The parsed response data.
        """
        return self._parse_many(
            BillingSetup, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BillingSetup:
        """
        Performs a POST request against the /finance/billingSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingSetup: The parsed response data.
        """
        return self._parse_one(
            BillingSetup, super()._make_request("POST", data=data, params=params).json()
        )
