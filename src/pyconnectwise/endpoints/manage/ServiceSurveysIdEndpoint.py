from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdCopyEndpoint import ServiceSurveysIdCopyEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsEndpoint import ServiceSurveysIdQuestionsEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdResultsEndpoint import ServiceSurveysIdResultsEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdUsagesEndpoint import ServiceSurveysIdUsagesEndpoint
from pyconnectwise.models.manage import ServiceSurvey
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSurveysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.copy = self._register_child_endpoint(ServiceSurveysIdCopyEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(ServiceSurveysIdUsagesEndpoint(client, parent_endpoint=self))
        self.results = self._register_child_endpoint(ServiceSurveysIdResultsEndpoint(client, parent_endpoint=self))
        self.questions = self._register_child_endpoint(ServiceSurveysIdQuestionsEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ServiceSurvey]:
        """
        Performs a GET request against the /service/surveys/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSurvey]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceSurvey, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurvey:
        """
        Performs a GET request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurvey: The parsed response data.
        """
        return self._parse_one(ServiceSurvey, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurvey:
        """
        Performs a PUT request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurvey: The parsed response data.
        """
        return self._parse_one(ServiceSurvey, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurvey:
        """
        Performs a PATCH request against the /service/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurvey: The parsed response data.
        """
        return self._parse_one(ServiceSurvey, super()._make_request("PATCH", data=data, params=params).json())
