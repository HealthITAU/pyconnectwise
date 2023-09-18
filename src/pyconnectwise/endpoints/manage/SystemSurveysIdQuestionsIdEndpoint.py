from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsIdValuesEndpoint import \
    SystemSurveysIdQuestionsIdValuesEndpoint
from pyconnectwise.models.manage import SurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSurveysIdQuestionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.values = self._register_child_endpoint(
            SystemSurveysIdQuestionsIdValuesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SurveyQuestion]:
        """
        Performs a GET request against the /system/surveys/{id}/questions/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyQuestion]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SurveyQuestion, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyQuestion:
        """
        Performs a GET request against the /system/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestion: The parsed response data.
        """
        return self._parse_one(SurveyQuestion, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /system/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyQuestion:
        """
        Performs a PUT request against the /system/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestion: The parsed response data.
        """
        return self._parse_one(SurveyQuestion, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyQuestion:
        """
        Performs a PATCH request against the /system/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestion: The parsed response data.
        """
        return self._parse_one(SurveyQuestion, super()._make_request("PATCH", data=data, params=params).json())
