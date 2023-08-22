from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import ServiceSurvey
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSurveysIdCopyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "copy", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurvey:
        """
        Performs a POST request against the /service/surveys/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurvey: The parsed response data.
        """
        return self._parse_one(ServiceSurvey, super()._make_request("POST", data=data, params=params).json())
