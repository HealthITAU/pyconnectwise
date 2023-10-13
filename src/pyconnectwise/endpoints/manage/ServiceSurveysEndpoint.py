from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysCountEndpoint import ServiceSurveysCountEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdEndpoint import ServiceSurveysIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ServiceSurvey
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceSurveysEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceSurvey], ConnectWiseManageRequestParams],
    IPostable[ServiceSurvey, ConnectWiseManageRequestParams],
    IPaginateable[ServiceSurvey, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "surveys", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ServiceSurvey])
        IPostable.__init__(self, ServiceSurvey)
        IPaginateable.__init__(self, ServiceSurvey)

        self.count = self._register_child_endpoint(ServiceSurveysCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSurveysIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSurveysIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSurveysIdEndpoint: The initialized ServiceSurveysIdEndpoint object.
        """
        child = ServiceSurveysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ServiceSurvey]:
        """
        Performs a GET request against the /service/surveys endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSurvey]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceSurvey, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ServiceSurvey]:
        """
        Performs a GET request against the /service/surveys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSurvey]: The parsed response data.
        """
        return self._parse_many(ServiceSurvey, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ServiceSurvey:
        """
        Performs a POST request against the /service/surveys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurvey: The parsed response data.
        """
        return self._parse_one(ServiceSurvey, super()._make_request("POST", data=data, params=params).json())
