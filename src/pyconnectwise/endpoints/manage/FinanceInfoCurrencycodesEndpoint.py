from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoCurrencycodesCountEndpoint import FinanceInfoCurrencycodesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoCurrencycodesIdEndpoint import FinanceInfoCurrencycodesIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import CurrencyCode
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceInfoCurrencycodesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CurrencyCode], ConnectWiseManageRequestParams],
    IPaginateable[CurrencyCode, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "currencyCodes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CurrencyCode])
        IPaginateable.__init__(self, CurrencyCode)

        self.count = self._register_child_endpoint(FinanceInfoCurrencycodesCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> FinanceInfoCurrencycodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInfoCurrencycodesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceInfoCurrencycodesIdEndpoint: The initialized FinanceInfoCurrencycodesIdEndpoint object.
        """
        child = FinanceInfoCurrencycodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CurrencyCode]:
        """
        Performs a GET request against the /finance/info/currencyCodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CurrencyCode]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CurrencyCode, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CurrencyCode]:
        """
        Performs a GET request against the /finance/info/currencyCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CurrencyCode]: The parsed response data.
        """
        return self._parse_many(CurrencyCode, super()._make_request("GET", data=data, params=params).json())
