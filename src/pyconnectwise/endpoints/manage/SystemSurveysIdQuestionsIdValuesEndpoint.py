from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsIdValuesIdEndpoint import \
    SystemSurveysIdQuestionsIdValuesIdEndpoint
from pyconnectwise.models.manage import SurveyQuestionValue
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSurveysIdQuestionsIdValuesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "values", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemSurveysIdQuestionsIdValuesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSurveysIdQuestionsIdValuesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSurveysIdQuestionsIdValuesIdEndpoint: The initialized SystemSurveysIdQuestionsIdValuesIdEndpoint object.
        """
        child = SystemSurveysIdQuestionsIdValuesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SurveyQuestionValue]:
        """
        Performs a GET request against the /system/surveys/{id}/questions/{id}/values endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyQuestionValue]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SurveyQuestionValue, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SurveyQuestionValue]:
        """
        Performs a GET request against the /system/surveys/{id}/questions/{id}/values endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyQuestionValue]: The parsed response data.
        """
        return self._parse_many(SurveyQuestionValue, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyQuestionValue:
        """
        Performs a POST request against the /system/surveys/{id}/questions/{id}/values endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestionValue: The parsed response data.
        """
        return self._parse_one(SurveyQuestionValue, super()._make_request("POST", data=data, params=params).json())
