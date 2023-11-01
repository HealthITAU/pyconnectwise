from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceDeliverymethodsCountEndpoint import (
    FinanceDeliverymethodsCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceDeliverymethodsIdEndpoint import (
    FinanceDeliverymethodsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import DeliveryMethod
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceDeliverymethodsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[DeliveryMethod], ConnectWiseManageRequestParams],
    IPostable[DeliveryMethod, ConnectWiseManageRequestParams],
    IPaginateable[DeliveryMethod, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "deliveryMethods", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[DeliveryMethod])
        IPostable.__init__(self, DeliveryMethod)
        IPaginateable.__init__(self, DeliveryMethod)

        self.count = self._register_child_endpoint(
            FinanceDeliverymethodsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceDeliverymethodsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceDeliverymethodsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceDeliverymethodsIdEndpoint: The initialized FinanceDeliverymethodsIdEndpoint object.
        """
        child = FinanceDeliverymethodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[DeliveryMethod]:
        """
        Performs a GET request against the /finance/deliveryMethods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DeliveryMethod]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            DeliveryMethod,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[DeliveryMethod]:
        """
        Performs a GET request against the /finance/deliveryMethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DeliveryMethod]: The parsed response data.
        """
        return self._parse_many(
            DeliveryMethod,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> DeliveryMethod:
        """
        Performs a POST request against the /finance/deliveryMethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DeliveryMethod: The parsed response data.
        """
        return self._parse_one(
            DeliveryMethod,
            super()._make_request("POST", data=data, params=params).json(),
        )
