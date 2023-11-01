from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingtermsCountEndpoint import (
    FinanceBillingtermsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceBillingtermsIdEndpoint import (
    FinanceBillingtermsIdEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceBillingtermsInfoEndpoint import (
    FinanceBillingtermsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import BillingTerm
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceBillingtermsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BillingTerm], ConnectWiseManageRequestParams],
    IPostable[BillingTerm, ConnectWiseManageRequestParams],
    IPaginateable[BillingTerm, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "billingTerms", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BillingTerm])
        IPostable.__init__(self, BillingTerm)
        IPaginateable.__init__(self, BillingTerm)

        self.count = self._register_child_endpoint(
            FinanceBillingtermsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            FinanceBillingtermsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceBillingtermsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingtermsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingtermsIdEndpoint: The initialized FinanceBillingtermsIdEndpoint object.
        """
        child = FinanceBillingtermsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BillingTerm]:
        """
        Performs a GET request against the /finance/billingTerms endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingTerm]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BillingTerm,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BillingTerm]:
        """
        Performs a GET request against the /finance/billingTerms endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingTerm]: The parsed response data.
        """
        return self._parse_many(
            BillingTerm, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BillingTerm:
        """
        Performs a POST request against the /finance/billingTerms endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingTerm: The parsed response data.
        """
        return self._parse_one(
            BillingTerm, super()._make_request("POST", data=data, params=params).json()
        )
