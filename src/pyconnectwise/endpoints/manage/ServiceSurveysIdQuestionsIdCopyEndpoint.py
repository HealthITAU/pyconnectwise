from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ServiceSurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceSurveysIdQuestionsIdCopyEndpoint(
    ConnectWiseEndpoint, IPostable[ServiceSurveyQuestion, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "copy", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, ServiceSurveyQuestion)

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ServiceSurveyQuestion:
        """
        Performs a POST request against the /service/surveys/{id}/questions/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(ServiceSurveyQuestion, super()._make_request("POST", data=data, params=params).json())
