from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsCountEndpoint import (
    SystemSurveysIdQuestionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsIdEndpoint import (
    SystemSurveysIdQuestionsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import SurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemSurveysIdQuestionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SurveyQuestion], ConnectWiseManageRequestParams],
    IPostable[SurveyQuestion, ConnectWiseManageRequestParams],
    IPaginateable[SurveyQuestion, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "questions", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[SurveyQuestion])
        IPostable.__init__(self, SurveyQuestion)
        IPaginateable.__init__(self, SurveyQuestion)

        self.count = self._register_child_endpoint(
            SystemSurveysIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemSurveysIdQuestionsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemSurveysIdQuestionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSurveysIdQuestionsIdEndpoint: The initialized SystemSurveysIdQuestionsIdEndpoint object.
        """
        child = SystemSurveysIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[SurveyQuestion]:
        """
        Performs a GET request against the /system/surveys/{id}/questions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyQuestion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SurveyQuestion,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[SurveyQuestion]:
        """
        Performs a GET request against the /system/surveys/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyQuestion]: The parsed response data.
        """
        return self._parse_many(
            SurveyQuestion,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SurveyQuestion:
        """
        Performs a POST request against the /system/surveys/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestion: The parsed response data.
        """
        return self._parse_one(
            SurveyQuestion,
            super()._make_request("POST", data=data, params=params).json(),
        )
