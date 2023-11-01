from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsCountEndpoint import (
    ServiceSurveysIdQuestionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdEndpoint import (
    ServiceSurveysIdQuestionsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ServiceSurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceSurveysIdQuestionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceSurveyQuestion], ConnectWiseManageRequestParams],
    IPostable[ServiceSurveyQuestion, ConnectWiseManageRequestParams],
    IPaginateable[ServiceSurveyQuestion, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "questions", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ServiceSurveyQuestion])
        IPostable.__init__(self, ServiceSurveyQuestion)
        IPaginateable.__init__(self, ServiceSurveyQuestion)

        self.count = self._register_child_endpoint(
            ServiceSurveysIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceSurveysIdQuestionsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServiceSurveysIdQuestionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSurveysIdQuestionsIdEndpoint: The initialized ServiceSurveysIdQuestionsIdEndpoint object.
        """
        child = ServiceSurveysIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ServiceSurveyQuestion]:
        """
        Performs a GET request against the /service/surveys/{id}/questions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSurveyQuestion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ServiceSurveyQuestion,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ServiceSurveyQuestion]:
        """
        Performs a GET request against the /service/surveys/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSurveyQuestion]: The parsed response data.
        """
        return self._parse_many(
            ServiceSurveyQuestion,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceSurveyQuestion:
        """
        Performs a POST request against the /service/surveys/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(
            ServiceSurveyQuestion,
            super()._make_request("POST", data=data, params=params).json(),
        )
