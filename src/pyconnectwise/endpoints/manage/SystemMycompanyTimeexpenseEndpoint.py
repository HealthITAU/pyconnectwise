from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyTimeexpenseCountEndpoint import \
    SystemMycompanyTimeexpenseCountEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyTimeexpenseIdEndpoint import SystemMycompanyTimeexpenseIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TimeExpense
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMycompanyTimeexpenseEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TimeExpense], ConnectWiseManageRequestParams],
    IPaginateable[TimeExpense, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "timeExpense", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TimeExpense])
        IPaginateable.__init__(self, TimeExpense)

        self.count = self._register_child_endpoint(
            SystemMycompanyTimeexpenseCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMycompanyTimeexpenseIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyTimeexpenseIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyTimeexpenseIdEndpoint: The initialized SystemMycompanyTimeexpenseIdEndpoint object.
        """
        child = SystemMycompanyTimeexpenseIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TimeExpense]:
        """
        Performs a GET request against the /system/myCompany/timeExpense endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeExpense]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimeExpense, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[TimeExpense]:
        """
        Performs a GET request against the /system/myCompany/timeExpense endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeExpense]: The parsed response data.
        """
        return self._parse_many(TimeExpense, super()._make_request("GET", data=data, params=params).json())
