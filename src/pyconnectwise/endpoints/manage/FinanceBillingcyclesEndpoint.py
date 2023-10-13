from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingcyclesCountEndpoint import FinanceBillingcyclesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingcyclesIdEndpoint import FinanceBillingcyclesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingcyclesInfoEndpoint import FinanceBillingcyclesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BillingCycle
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceBillingcyclesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BillingCycle], ConnectWiseManageRequestParams],
    IPostable[BillingCycle, ConnectWiseManageRequestParams],
    IPaginateable[BillingCycle, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "billingCycles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BillingCycle])
        IPostable.__init__(self, BillingCycle)
        IPaginateable.__init__(self, BillingCycle)

        self.count = self._register_child_endpoint(FinanceBillingcyclesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(FinanceBillingcyclesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceBillingcyclesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingcyclesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingcyclesIdEndpoint: The initialized FinanceBillingcyclesIdEndpoint object.
        """
        child = FinanceBillingcyclesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BillingCycle]:
        """
        Performs a GET request against the /finance/billingCycles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingCycle]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BillingCycle, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[BillingCycle]:
        """
        Performs a GET request against the /finance/billingCycles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingCycle]: The parsed response data.
        """
        return self._parse_many(BillingCycle, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BillingCycle:
        """
        Performs a POST request against the /finance/billingCycles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingCycle: The parsed response data.
        """
        return self._parse_one(BillingCycle, super()._make_request("POST", data=data, params=params).json())
