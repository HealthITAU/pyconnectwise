from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeSheetsIdApproveEndpoint import (
    TimeSheetsIdApproveEndpoint,
)
from pyconnectwise.endpoints.manage.TimeSheetsIdAuditsEndpoint import (
    TimeSheetsIdAuditsEndpoint,
)
from pyconnectwise.endpoints.manage.TimeSheetsIdRejectEndpoint import (
    TimeSheetsIdRejectEndpoint,
)
from pyconnectwise.endpoints.manage.TimeSheetsIdReverseEndpoint import (
    TimeSheetsIdReverseEndpoint,
)
from pyconnectwise.endpoints.manage.TimeSheetsIdSubmitEndpoint import (
    TimeSheetsIdSubmitEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import TimeSheet
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class TimeSheetsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[TimeSheet, ConnectWiseManageRequestParams],
    IPaginateable[TimeSheet, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, TimeSheet)
        IPaginateable.__init__(self, TimeSheet)

        self.submit = self._register_child_endpoint(
            TimeSheetsIdSubmitEndpoint(client, parent_endpoint=self)
        )
        self.audits = self._register_child_endpoint(
            TimeSheetsIdAuditsEndpoint(client, parent_endpoint=self)
        )
        self.reject = self._register_child_endpoint(
            TimeSheetsIdRejectEndpoint(client, parent_endpoint=self)
        )
        self.approve = self._register_child_endpoint(
            TimeSheetsIdApproveEndpoint(client, parent_endpoint=self)
        )
        self.reverse = self._register_child_endpoint(
            TimeSheetsIdReverseEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TimeSheet]:
        """
        Performs a GET request against the /time/sheets/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeSheet]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TimeSheet,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TimeSheet:
        """
        Performs a GET request against the /time/sheets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeSheet: The parsed response data.
        """
        return self._parse_one(
            TimeSheet, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /time/sheets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
