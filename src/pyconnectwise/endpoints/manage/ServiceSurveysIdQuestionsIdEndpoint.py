from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdCopyEndpoint import \
    ServiceSurveysIdQuestionsIdCopyEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdOptionsEndpoint import \
    ServiceSurveysIdQuestionsIdOptionsEndpoint
from pyconnectwise.models.manage import ServiceSurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSurveysIdQuestionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.options = self._register_child_endpoint(
            ServiceSurveysIdQuestionsIdOptionsEndpoint(client, parent_endpoint=self)
        )
        self.copy = self._register_child_endpoint(ServiceSurveysIdQuestionsIdCopyEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ServiceSurveyQuestion]:
        """
        Performs a GET request against the /service/surveys/{id}/questions/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyQuestion:
        """
        Performs a GET request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(ServiceSurveyQuestion, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyQuestion:
        """
        Performs a PUT request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(ServiceSurveyQuestion, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyQuestion:
        """
        Performs a PATCH request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(ServiceSurveyQuestion, super()._make_request("PATCH", data=data, params=params).json())
