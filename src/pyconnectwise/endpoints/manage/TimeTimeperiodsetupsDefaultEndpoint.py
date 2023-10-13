from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TimePeriodSetupDefaults
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class TimeTimeperiodsetupsDefaultEndpoint(
    ConnectWiseEndpoint,
    IGettable[TimePeriodSetupDefaults, ConnectWiseManageRequestParams],
    IPaginateable[TimePeriodSetupDefaults, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "default", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TimePeriodSetupDefaults)
        IPaginateable.__init__(self, TimePeriodSetupDefaults)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TimePeriodSetupDefaults]:
        """
        Performs a GET request against the /time/timePeriodSetups/default endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimePeriodSetupDefaults]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimePeriodSetupDefaults, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> TimePeriodSetupDefaults:
        """
        Performs a GET request against the /time/timePeriodSetups/default endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimePeriodSetupDefaults: The parsed response data.
        """
        return self._parse_one(TimePeriodSetupDefaults, super()._make_request("GET", data=data, params=params).json())
