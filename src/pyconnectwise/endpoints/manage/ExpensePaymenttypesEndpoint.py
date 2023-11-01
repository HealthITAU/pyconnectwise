from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymenttypesCountEndpoint import (
    ExpensePaymenttypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ExpensePaymenttypesIdEndpoint import (
    ExpensePaymenttypesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ExpensePaymenttypesInfoEndpoint import (
    ExpensePaymenttypesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import PaymentType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ExpensePaymenttypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PaymentType], ConnectWiseManageRequestParams],
    IPostable[PaymentType, ConnectWiseManageRequestParams],
    IPaginateable[PaymentType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "paymentTypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PaymentType])
        IPostable.__init__(self, PaymentType)
        IPaginateable.__init__(self, PaymentType)

        self.count = self._register_child_endpoint(
            ExpensePaymenttypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ExpensePaymenttypesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ExpensePaymenttypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpensePaymenttypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpensePaymenttypesIdEndpoint: The initialized ExpensePaymenttypesIdEndpoint object.
        """
        child = ExpensePaymenttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PaymentType]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PaymentType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PaymentType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[PaymentType]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PaymentType]: The parsed response data.
        """
        return self._parse_many(
            PaymentType, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaymentType:
        """
        Performs a POST request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaymentType: The parsed response data.
        """
        return self._parse_one(
            PaymentType, super()._make_request("POST", data=data, params=params).json()
        )
