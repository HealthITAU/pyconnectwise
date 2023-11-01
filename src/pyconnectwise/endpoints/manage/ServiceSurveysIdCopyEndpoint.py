from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import ServiceSurvey
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceSurveysIdCopyEndpoint(
    ConnectWiseEndpoint, IPostable[ServiceSurvey, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "copy", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, ServiceSurvey)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceSurvey:
        """
        Performs a POST request against the /service/surveys/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurvey: The parsed response data.
        """
        return self._parse_one(
            ServiceSurvey,
            super()._make_request("POST", data=data, params=params).json(),
        )
