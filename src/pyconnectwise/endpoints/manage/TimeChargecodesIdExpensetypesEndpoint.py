from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesIdExpensetypesCountEndpoint import (
    TimeChargecodesIdExpensetypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.TimeChargecodesIdExpensetypesIdEndpoint import (
    TimeChargecodesIdExpensetypesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ChargeCodeExpenseType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class TimeChargecodesIdExpensetypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ChargeCodeExpenseType], ConnectWiseManageRequestParams],
    IPostable[ChargeCodeExpenseType, ConnectWiseManageRequestParams],
    IPaginateable[ChargeCodeExpenseType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "expenseTypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ChargeCodeExpenseType])
        IPostable.__init__(self, ChargeCodeExpenseType)
        IPaginateable.__init__(self, ChargeCodeExpenseType)

        self.count = self._register_child_endpoint(
            TimeChargecodesIdExpensetypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> TimeChargecodesIdExpensetypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized TimeChargecodesIdExpensetypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeChargecodesIdExpensetypesIdEndpoint: The initialized TimeChargecodesIdExpensetypesIdEndpoint object.
        """
        child = TimeChargecodesIdExpensetypesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ChargeCodeExpenseType]:
        """
        Performs a GET request against the /time/chargeCodes/{id}/expenseTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChargeCodeExpenseType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ChargeCodeExpenseType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ChargeCodeExpenseType]:
        """
        Performs a GET request against the /time/chargeCodes/{id}/expenseTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChargeCodeExpenseType]: The parsed response data.
        """
        return self._parse_many(
            ChargeCodeExpenseType,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ChargeCodeExpenseType:
        """
        Performs a POST request against the /time/chargeCodes/{id}/expenseTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChargeCodeExpenseType: The parsed response data.
        """
        return self._parse_one(
            ChargeCodeExpenseType,
            super()._make_request("POST", data=data, params=params).json(),
        )
