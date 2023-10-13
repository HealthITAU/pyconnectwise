from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysInfoCountEndpoint import SystemSurveysInfoCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import SurveyInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemSurveysInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SurveyInfo], ConnectWiseManageRequestParams],
    IPaginateable[SurveyInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SurveyInfo])
        IPaginateable.__init__(self, SurveyInfo)

        self.count = self._register_child_endpoint(SystemSurveysInfoCountEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[SurveyInfo]:
        """
        Performs a GET request against the /system/surveys/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), SurveyInfo, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[SurveyInfo]:
        """
        Performs a GET request against the /system/surveys/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyInfo]: The parsed response data.
        """
        return self._parse_many(SurveyInfo, super()._make_request("GET", data=data, params=params).json())
