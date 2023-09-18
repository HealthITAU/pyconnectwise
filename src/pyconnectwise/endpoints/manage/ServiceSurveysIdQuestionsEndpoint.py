from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsCountEndpoint import ServiceSurveysIdQuestionsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdEndpoint import ServiceSurveysIdQuestionsIdEndpoint
from pyconnectwise.models.manage import ServiceSurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSurveysIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "questions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceSurveysIdQuestionsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSurveysIdQuestionsIdEndpoint:
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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceSurveyQuestion, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceSurveyQuestion]:
        """
        Performs a GET request against the /service/surveys/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSurveyQuestion]: The parsed response data.
        """
        return self._parse_many(ServiceSurveyQuestion, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyQuestion:
        """
        Performs a POST request against the /service/surveys/{id}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(ServiceSurveyQuestion, super()._make_request("POST", data=data, params=params).json())
