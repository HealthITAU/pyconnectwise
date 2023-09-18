from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdResultsCountEndpoint import ServiceSurveysIdResultsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdResultsIdEndpoint import ServiceSurveysIdResultsIdEndpoint
from pyconnectwise.models.manage import SurveyResult
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSurveysIdResultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "results", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceSurveysIdResultsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSurveysIdResultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSurveysIdResultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSurveysIdResultsIdEndpoint: The initialized ServiceSurveysIdResultsIdEndpoint object.
        """
        child = ServiceSurveysIdResultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SurveyResult]:
        """
        Performs a GET request against the /service/surveys/{id}/results endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyResult]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SurveyResult, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SurveyResult]:
        """
        Performs a GET request against the /service/surveys/{id}/results endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyResult]: The parsed response data.
        """
        return self._parse_many(SurveyResult, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyResult:
        """
        Performs a POST request against the /service/surveys/{id}/results endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyResult: The parsed response data.
        """
        return self._parse_one(SurveyResult, super()._make_request("POST", data=data, params=params).json())
