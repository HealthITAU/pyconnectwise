from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceCurrenciesCountEndpoint import (
    FinanceCurrenciesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceCurrenciesIdEndpoint import (
    FinanceCurrenciesIdEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceCurrenciesInfoEndpoint import (
    FinanceCurrenciesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import FinanceCurrency
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceCurrenciesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[FinanceCurrency], ConnectWiseManageRequestParams],
    IPostable[FinanceCurrency, ConnectWiseManageRequestParams],
    IPaginateable[FinanceCurrency, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "currencies", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[FinanceCurrency])
        IPostable.__init__(self, FinanceCurrency)
        IPaginateable.__init__(self, FinanceCurrency)

        self.count = self._register_child_endpoint(
            FinanceCurrenciesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            FinanceCurrenciesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceCurrenciesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceCurrenciesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceCurrenciesIdEndpoint: The initialized FinanceCurrenciesIdEndpoint object.
        """
        child = FinanceCurrenciesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[FinanceCurrency]:
        """
        Performs a GET request against the /finance/currencies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[FinanceCurrency]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            FinanceCurrency,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[FinanceCurrency]:
        """
        Performs a GET request against the /finance/currencies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[FinanceCurrency]: The parsed response data.
        """
        return self._parse_many(
            FinanceCurrency,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> FinanceCurrency:
        """
        Performs a POST request against the /finance/currencies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            FinanceCurrency: The parsed response data.
        """
        return self._parse_one(
            FinanceCurrency,
            super()._make_request("POST", data=data, params=params).json(),
        )
