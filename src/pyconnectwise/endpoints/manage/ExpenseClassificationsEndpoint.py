from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseClassificationsCountEndpoint import (
    ExpenseClassificationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ExpenseClassificationsIdEndpoint import (
    ExpenseClassificationsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Classification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ExpenseClassificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Classification], ConnectWiseManageRequestParams],
    IPaginateable[Classification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "classifications", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Classification])
        IPaginateable.__init__(self, Classification)

        self.count = self._register_child_endpoint(
            ExpenseClassificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ExpenseClassificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseClassificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseClassificationsIdEndpoint: The initialized ExpenseClassificationsIdEndpoint object.
        """
        child = ExpenseClassificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Classification]:
        """
        Performs a GET request against the /expense/classifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Classification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Classification,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Classification]:
        """
        Performs a GET request against the /expense/classifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Classification]: The parsed response data.
        """
        return self._parse_many(
            Classification,
            super()._make_request("GET", data=data, params=params).json(),
        )
